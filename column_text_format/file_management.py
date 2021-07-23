import os
import boto3
from contextlib import contextmanager

def open_iterator(file_name, bucket_name=None):
    '''Returns an iterator either from the file object or from the s3 object
    Both have tne \n at the end, which must be handled elsewhere in this class'''
    if (bucket_name == None):
        iterator = open(file_name)
    else:
        session = boto3.Session().resource('s3')
        s3_obj = session.Object(bucket_name, file_name)
        body = s3_obj.get()['Body']
        iterator = body.iter_lines(chunk_size=1024, keepends=True)
    return iterator

def full_file(file_name, bucket_name=None):
    '''Returns an iterator either from the file object or from the s3 object
    Both have tne \n at the end, which must be handled elsewhere in this class'''
    string = ''
    if (bucket_name == None):
        iterator = open(file_name)
        for line in iterator:
            string += line
    else:
        session = boto3.Session().resource('s3')
        s3_obj = session.Object(bucket_name, file_name)
        body = s3_obj.get()['Body']
        iterator = body.iter_lines(chunk_size=1024, keepends=True)
        for line in iterator:
            string += line.decode('utf8')
    return string

def list_files(folder_name, bucket_name=None):
    files = []
    if (bucket_name == None):
        for each_file in os.listdir(folder_name):
            if(each_file[-4:] == '.txt'):
                files.append(os.path.join(folder_name, each_file))
    else:
        session = boto3.Session().resource('s3')
        s3_obj = session.Object(bucket_name, folder_name)
        for obj in s3_obj.Bucket().objects.all():
            if(obj.key[-4:] == '.txt'):
                files.append(obj.key)
    return files

def get_file_name(file_path):
    '''Removes trailing structure and extension to just return the file name'''
    base=os.path.basename(file_path)
    return os.path.splitext(base)[0]
