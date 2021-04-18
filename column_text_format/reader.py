import csv
import os
import time
import glob
import json
from .column import Column

class Reader:
    '''
    This class will be used to convert to and from Ctf files
    '''

    def __init__(self, file_name):
        self.file_name = file_name
        self.columns = []
        self.data_types = {}

        for each_file in os.listdir(file_name):
            if(each_file[-4:] == '.txt'):
                self.columns.append(each_file[:-4])
        self.read_metadata()

    def __getitem__(self, column_key):
        '''Treats data like a dictionary, retuns iter when called as ctf_file['column']'''
        full_path = os.path.join(self.file_name, column_key)
        try:
            return Column(full_path, self.data_types[column_key])
        except:
            print("err") #!
            return Column(full_path)

    def __iter__(self):
        '''Will return an iterable of all columns'''
        self.columns = []
        subpath = os.path.join(self.file_name, '*')
        for column_file in glob.glob(subpath):
            self.columns.append(iter(Column(column_file)))
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
            metadata_file = self.file_name + "/" + self.file_name + "-metadata.json"
        with open(metadata_file) as file:
            json_data = json.load(file)
        for column_file in json_data["tableSchema"]["columnFiles"]:
            column_name = column_file["titles"]
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
