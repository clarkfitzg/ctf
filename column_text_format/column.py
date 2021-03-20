import os


class Column:
    '''
    The column object is returned as an iterable for each column that needs to be accessed. 
    For multiple columns a list of Column objects should be returned.

    Attributes:
        file_name(str): The full path to the colum file
        data_type(type): The type of data in the column as specified in metadata.json
        column_file(_io.TextIOWrapper): Refers to the opened file
    '''


    def __init__(self, file_name, data_type = str):
        '''Sets up the column name that will be accessed'''
        file_name_only, extension = os.path.splitext(file_name)
        if (extension == ''):
            self.file_name = file_name + ".txt"
        else:
            self.file_name = file_name
        if (not os.path.exists(self.file_name)):
            raise FileNotFoundError(f'{self.file_name} does not exist')
        self.data_type = data_type

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

        if not type(row) is self.data_type:
            row = self.convert_data_type(row)
        return row

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

    def convert_data_type(self, value):
        '''Converts value to the data_type found in metadata.json'''
        self.data_type(value)
