import time
import matplotlib.pyplot as plt
import numpy as np
import csv
import re

from column_text_format import reader

ctf_file = '/home/ec2-user/GDELT'
csv_file = '/mnt/extra/2018.csv'
delimiter = "\t"

sacramento_regex = re.compile('sacramento', flags=re.IGNORECASE)

def get_ctf_time(ctf_file):
    total = 0
    start = time.time()
    ctf_reader = reader(ctf_file)
    location_column = ctf_reader['column37']
    for row in location_column:
        if(re.search(sacramento_regex, row)):
            total+=1
    end = time.time()
    total_time = end-start
    print("CTF time: " + repr(total_time))
    print("Occurances of 'sacramento'" + repr(total))

def get_csv_time(ctf_file):
    total = 0
    start = time.time()
    with open(csv_file) as csv_file:
        reader = csv.reader(csv_file, delimiter=delimiter)
        for row in reader:
            if(re.search(sacramento_regex, row[36])):
                total+=1
    end = time.time()
    total_time = end-start
    print("CSV time: " + repr(total_time))
    print("Occurances of 'sacramento'" + repr(total))

get_ctf_time(ctf_file)
get_csv_time(csv_file)