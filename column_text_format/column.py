import os
from .metadata_conversion_funcs import metadata_types

class Column:
    '''
    The column object is returned as an iterable for each column that needs to be accessed. 
    For multiple columns a list of Column objects should be returned.

    Attributes:
        file_name(str): The full path to the colum file
        datatype(dict): The type of data in the column as specified in metadata.json
        column_file(_io.TextIOWrapper): Refers to the opened file
    '''

    def __init__(self, file_name, datatype = None):
        '''Sets up the column name that will be accessed'''
        self.datatype = ""
        self.file_name = ""

        file_name_only, extension = os.path.splitext(file_name)
        if (extension == ''):
            self.file_name = file_name + ".txt"
        else:
            self.file_name = file_name
        if (not os.path.exists(self.file_name)):
            raise FileNotFoundError(f'{self.file_name} does not exist')
        self.datatype = datatype

    def __iter__(self):
        '''Sets up the object for iteration'''
        self.column_file = open(self.file_name)
        return self

    def __next__(self):
        '''Returns the next item in the column converted to the proper data type'''
        try:
            row = next(self.column_file)[:-1]
        except StopIteration:
            self.column_file.close()
            raise StopIteration()

        return self.parse_data(row)

    def __len__(self):
        '''Returns the length of the column without loading the data into memory'''
        with open(self.file_name) as opened_file:
            for index, value in enumerate(opened_file):
                pass
        self.length = index
        return self.length

    def __del__(self):
        '''Runs when self is destroyed, it closes the open file'''
        self.close()

    def close(self):
        '''closes self.column_file'''
        #self.column_file.close()

    def parse_data(self, value):
        if (self.datatype == None):
            return value
        else:
            try:
                conversion_func = metadata_types[self.datatype]
            except KeyError as err:
                raise NotImplementedError(self.datatype+" is not currently a valid datatype") from None
            return conversion_func(value)

    # def convert_data_type(self, value):
    #     '''Converts value to the data_type found in metadata.json'''
    #     return self.data_type(value)
