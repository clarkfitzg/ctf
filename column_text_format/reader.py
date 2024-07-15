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
"""Legacy code. Kept temporarily as context.
class Reader:
    '''
    This class will be used to convert to and from Ctf files
    '''

    def __init__(self, file_path, bucket_name=None):
        self.file_path = file_path
        self.file_name = os.path.basename(self.file_path)
        self.columns = []
        self.column_files = list_files(self.file_path, bucket_name)
        self.data_types = {}
        self.bucket_name = bucket_name

        # self.read_metadata()
        for column_file in self.column_files:
            self.columns.append(iter(Column(column_file, bucket_name=self.bucket_name)))

    def __getitem__(self, column_key):
        '''Treats data like a dictionary, retuns iter when called as ctf_file['column']'''
        full_path = os.path.join(self.file_path, column_key + '.txt')
        try:
            return Column(full_path, self.data_types[column_key], bucket_name=self.bucket_name)
        except:
            # print("data type failed to pass for " + repr(column_key)) #!
            return Column(full_path, bucket_name=self.bucket_name)

    def __iter__(self):
        '''Will return an iterable of all columns'''
        for column_file in self.column_files:
            self.columns.append(iter(Column(column_file, bucket_name=self.bucket_name)))
        return self

    def __next__(self):
        '''Passes next to each iterable column'''
        row = []
        for column in self.columns:
            try:
                row.append(next(column))
            except StopIteration:
                column.close()
                raise StopIteration()
        return row

    def convert_local_files(self):
        '''Will run conversion on all .csv files in this directory'''
        print(f'name\tstart size\ttime')
        for csv_file in glob.glob('*.csv'):
            time = self.convert_csv_to_ctf(csv_file)
            file_size = os.path.getsize(csv_file)
            print(f'{csv_file}\t{file_size}\t{time:.2f}')


    def stream_convert_csv_to_ctf(self, stream, path, name, **kwargs):
        stream_convert_csv_to_ctf(stream, path, name, **kwargs)
        

    def convert_csv_to_ctf(self, csv_file):
        '''Conversion function for each .csv file'''
        total_columns = 0

        start = time.time()
        # Gets folder name from csv
        new_folder_name = os.path.splitext(csv_file)[0]
        if(not os.path.isdir(new_folder_name)):
            os.mkdir(new_folder_name)

        # Finds the total rows in the file
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if (len(row) > total_columns):
                    total_columns = len(row)

        # Writes rows to new files
        for i in range(0,total_columns):
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                column_file = os.path.join(new_folder_name, f'column{i+1}.txt')
                if (os.path.exists(column_file)):
                    os.remove(column_file)
                f = open(column_file, 'a')
                for row in reader:
                    f.write(row[i]+'\n')
                f.close()
        end = time.time()
        return end - start

    def load_columns(self, ctf_file, columns):
        '''
        file: the name of the folder what contains the columns
        columns: column names to return
        returns a list with the column values in it
        '''
        return_list = []
        for column in columns:
            return_list.append(self.load_column(ctf_file, column))
        return return_list

    def load_column(self, ctf_file, column):
        return_list = []
        # Get full path to ctf column
        column_file = os.path.join(ctf_file, column)
        # Finds the total rows in the file
        with open(column_file, 'r') as file:
            reader = csv.reader(file, delimiter='\n')
            for line in reader:
                try:
                    return_list.append(line[0])
                except Exception as e:
                    continue
        return return_list

    def read_metadata(self, metadata_file = None):
        '''When run this stores the metadata types for each column in self.data_types as a dictionary of keys with the column name and the value as the dataType from metadata.'''
        self.data_types = {}

        if(metadata_file == None):
            metadata_file = self.file_path + "/" + self.file_name + "-metadata.json"
        json_string = full_file(metadata_file, self.bucket_name)
        json_data = json.loads(json_string)
        for column_file in json_data["tableSchema"]["columnFiles"]:
            column_name = os.path.splitext(column_file["url"])[0]
            try:
                column_type = column_file["datatype"]
                self.data_types[column_name] = column_type
            except:
                pass


def stream_convert_csv_to_ctf(stream, path, name, **kwargs):
    # TODO (2nd): add reader argument, maybe use kwargs
    r = csv.reader(iter(stream.readline, ''), **kwargs)

    firstRow = next(r)

    total_columns = len(firstRow)

    #makes the directory with user specified name and location

    path = os.path.join(path, name)

    os.mkdir(path)

    os.chdir(path)

    ctf_files = [] #array that will be used for looping through with zip


    #open a new file for each column and then append that to the ctf_files array
    for i in range(0,total_columns):
        outF = open(f'column{i+1}.txt', "w")
        ctf_files.append(outF)

    # TODO (1st): 
    # Create a list of open files, one for each column.
    # Then iterate through and write to these files.
    
    #write the first row 
    for value, ctf_file in zip(firstRow, ctf_files):
        ctf_file.write(value + "\n")
        #ctf_file.writeline(value) ??

    #write all the remaining 
    for row in r:
        for value, ctf_file in zip(row, ctf_files):
            ctf_file.write(value + "\n")
            #ctf_file.writeline(value) ??
"""

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