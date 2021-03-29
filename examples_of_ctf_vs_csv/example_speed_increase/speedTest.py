import time
import matplotlib.pyplot as plt
import numpy as np
import csv

from column_text_format import reader

def read_through_column(col):
    for item in col:
        pass

with open('vgsales.csv') as f:
    total_lines = sum(1 for line in f)

# get ctf access times
ctf_times = []

open_start = time.time()
vgsales = reader.Reader("vgsales")
vgsales.read_metadata()
open_end = time.time()
open_time = open_end - open_start
for i in range(1, len(vgsales.columns)):
    start = time.time()
    for col in vgsales.columns[0:i]:
        read_through_column(vgsales[col])
    end = time.time()
    ctf_times.append(end-start + open_time)

# get csv times
row_len = 0
csv_times = []
with open('vgsales.csv') as csv_file:
    reader = csv.reader(csv_file)
    x = iter(reader)
    row_len = len(next(x))

for i in range(1, row_len):
    start = time.time()
    with open('vgsales.csv') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            x = row[0:i]
            pass
    end = time.time()
    csv_times.append(end-start)

# Plot the times figure
fig = plt.figure()
plt.title("Time to access " + str(total_lines) + " rows of data")
plt.xlabel("Columns accessed")
plt.ylabel("Time")
plt.plot(ctf_times, label='ctf times')
plt.plot(csv_times, label='csv times')
plt.legend()
fig.savefig('csv_ctf_access_times.png')