import csv
import os
import time
import glob
import json
import pandas as pd

META_TYPE = "json"
NEWLINE = "\n"
FILETYPE = ".txt"
CONTEXT = ["http://www.w3.org/ns/csvw"]


def create(datasetName, location):
    colCounter = 0
    #TODO: check if legit dataset
    dataLoc = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/'+datasetName+'.csv'
    dataset = pd.read_csv(dataLoc)
    tableArray = []
    colArray = []
    for colName, col in dataset.items():
        colArray.append({'url': colName, 'titles': colName, 'datatype': str(dataset.dtypes[colName].name)})
        with open(colName+FILETYPE, 'w') as colWrite:
            for value in col:
                colWrite.write(str(value)+"\n")
    tableArray.append({'url':[datasetName+'.csv'], 'tableSchema':{'columns':colArray}})
    jsonDictionary = { '@context': CONTEXT, 'tables':tableArray}
    with open(datasetName+'.'+META_TYPE, 'w') as file:
        json.dump(jsonDictionary, file, ensure_ascii=False, indent=2)

def findMeta(location):
    metafile = None
    #Iterate through the files in the location.
    for root, dirs, files in os.walk(location):
        #check if any have the type used for metadata.
        for name in files:
            #Find the first file of the type used for metadata. Upon finding it, assign it to metafile and break.
            if name.endswith(META_TYPE):
                metafile = name
                break
    #If the directory doesn't have a metafile, throw an error and break.
    #Check how we want to do error logging
    #if(metafile == None):
        #TODO Print Error
    return metafile

#Read a ctf metadata file to create a dataframe. It will read nrows rows from each column file. 
def read(location, columns, numRows):
    metafile = findMeta(location)
    dataframe = None
    if(metafile != None):
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
    return dataframe