import os, json
from .column import Column
from .file_management import list_files, get_file_name

class Writer:
    '''This class will be used to read CTF files'''

    def __init__(self, file_path, bucket_name=None):
        self.file_path = file_path
        self.file_name = os.path.basename(self.file_path)
        self.column_file_objects = {} # Stores the file_objects for each column
        # self.columns = []
        self.data_types = {}
        # self.read_metadata()
        for column_file in list_files(self.file_path, bucket_name):
            print(column_file)
            key = get_file_name(column_file)
            print(key)
            self.column_file_objects[key] = open(column_file, "a")

    def write(self, data):
        # Checks to see if we are writing a list of values
        for key in data:
            self.column_file_objects[key].write(str(data[key]) + '\n')
            self.column_file_objects[key].close()

    def close(self):
        for key in self.column_file_objects:
            self.column_file_objects[key].close()