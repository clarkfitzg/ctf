import csv
import os
import sys
import time
import glob
import json
import pandas as pd

METASUFFIX='-metadata'
META_TYPE = "json"
NEWLINE = "\n"

def findMeta(location):
    metafile = None
    #Iterate through the files in the location.
    for root, dirs, files in os.walk(location):
        #check if any have the type used for metadata.
        for name in files:
            #Find the first file of the type used for metadata. Upon finding it, assign it to metafile and break.
            if name.endswith(METASUFFIX+'.'+META_TYPE):
                metafile = name
                break
    #If the directory doesn't have a metafile, throw an error and break.
    if(metafile == None):
        print("Unable to find a metafile within provided directory", file=sys.stderr)
    return metafile

#Read a ctf metadata file to create a dataframe. It will read nrows rows from each column file. 
def read(location, columns, numRows=None):
    if location.endswith(METASUFFIX+'.'+META_TYPE):
        metafile = location
    else:
        metafile = findMeta(location)
    dataframe = None
    if(metafile != None):
        try:
            file = open(metafile, "r")
            metadata = json.loads(file.read())
            for col in columns:
                #todo if col not in metafile
                #processes if the columns are selected as int.
                columnActual = None
                if isinstance(col, int):
                    columnActual = col
                else:
                    for columnID, metaColumns in enumerate(metadata['tables'][0]['tableSchema']['columns']):
                        if(metaColumns['titles']) == col:
                            columnActual=columnID
                if(columnActual != None):
                    colLocation = metadata['tables'][0]['tableSchema']['columns'][columnActual]['url']
                    colName = metadata['tables'][0]['tableSchema']['columns'][columnActual]['titles']
                    readColumn = pd.read_csv(colLocation+".txt", nrows=numRows)
                    readColumn.rename(columns={readColumn.columns[0]:colName}, inplace=True)
                    if dataframe is not None:
                        dataframe = pd.concat([dataframe, readColumn], axis=1)
                    else:
                        dataframe = readColumn
                else:
                    print(col+" was not found within the metadata file")
        except:
                print("Unable to open metafile.", file=sys.stderr)
    return dataframe