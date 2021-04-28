import time
import matplotlib.pyplot as plt
import numpy as np
import csv
import re

from column_text_format import reader

ctf_file = '/home/ec2-user/GDELT'
csv_file = '/mnt/extra/2018.csv'
delimiter = "\t"

sacramento_regex = re.compile('sacramento')

def get_ctf_time(ctf_file):
    total = 0
    start = time.time()
    ctf_reader = reader(ctf_file)
    location_column = ctf_reader['column37']
    for row in location_column:
        if(re.search(sacramento_regex, row, flags=re.IGNORECASE)):
            total+=1
            print(row)
    end = time.time()
    print(total)

get_ctf_time(ctf_file)