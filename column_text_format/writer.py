import os
from .file_management import list_files, open_iterator, full_file

class Writer:
    '''This class will be used to read CTF files'''

    def __init__(self, file_path, bucket_name=None):
        self.file_path = file_path
        self.file_name = os.path.basename(self.file_path)
        self.columns = []
        self.data_types = {}
        self.bucket_name = bucket_name
        self.file_name = os.path.basename(self.file_path)
        self.column_files = list_files(self.file_path, bucket_name)
        # self.read_metadata()
        for column_file in self.column_files:
            self.columns.append(iter(Column(column_file, bucket_name=self.bucket_name)))


    def write(self, write_dict):
        print(write_dict)



    