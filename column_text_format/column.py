import os
import boto3
from .metadata_conversion_funcs import metadata_types
from .file_management import open_iterator

class Column:
    '''
    The column object is returned as an iterable for each column that needs to be accessed. 
    For multiple columns a list of Column objects should be returned.

    Attributes:
        file_name(str): The full path to the colum file
        datatype(dict): The type of data in the column as specified in metadata.json
        column_file(_io.TextIOWrapper): Refers to the opened file
    '''

    def __init__(self, file_name, datatype = None, bucket_name=None):
        '''Sets up the column name that will be accessed'''
        self.datatype = datatype
        self.file_name = file_name
        self.bucket_name = bucket_name
        self.index_name = os.path.splitext(os.path.split(file_name)[1])[0]

        # file_name_only, extension = os.path.splitext(file_name)
        # if (extension == ''):
        #     self.file_name = file_name + ".txt"
        # else:
        #     self.file_name = file_name
        # if (not os.path.exists(self.file_name)):
        #     raise FileNotFoundError(f'{self.file_name} does not exist')
        self.datatype = datatype

    def __iter__(self):
        '''Sets up the object for iteration'''
        self.iterator = open_iterator(self.file_name, bucket_name=self.bucket_name)
        return self

    def __next__(self):
        '''Returns the next item in the column converted to the proper data type'''
        try:
            if (self.bucket_name == None):
                row = next(self.iterator)[:-1]
            else:
                row = next(self.iterator).decode('utf8')[:-1]
        except StopIteration:
            self.iterator.close()
            raise StopIteration()

        return self.parse_data(row)

    def __len__(self):
        '''Returns the length of the column without loading the data into memory'''
        opened_file = open_iterator(self.file_name, bucket_name=self.bucket_name)
        counter = 0
        for value in opened_file:
            counter+=1
        self.length = counter
        opened_file.close()
        return self.length

    def __del__(self):
        '''Runs when self is destroyed, it closes the open file'''
        pass
        # self.iterator.close()

    # def open_iterator(self, file_name):
    #     '''Returns an iterator either from the file object or from the s3 object
    #     Both have tne \n at the end, which must be handled elsewhere in this class'''
    #     if (not self.bucket_name):
    #         self.iterator = open(file_name)
    #     else:
    #         session = boto3.Session().resource('s3')
    #         s3_obj = session.Object(self.bucket_name, self.key)
    #         body = s3_obj.get()['Body']
    #         self.iterator = body.iter_lines(chunk_size=1024, keepends=True)
    #     return self.iterator

    def parse_data(self, value):
        if (self.datatype == None):
            return value
        else:
            try:
                conversion_func = metadata_types[self.datatype]
            except KeyError as err:
                raise NotImplementedError(self.datatype+" is not currently a valid datatype") from None
            return conversion_func(value)

