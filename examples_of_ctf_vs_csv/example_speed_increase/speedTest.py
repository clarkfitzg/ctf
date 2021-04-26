import time
import matplotlib.pyplot as plt
import numpy as np
import csv

from column_text_format import reader

def try_conversion(x):
    try:
        x = int(x)
    except:
        pass
    return x

# ctf_file = '/home/ec2-user/GDELT'
# csv_file = '/mnt/extra/2018.csv'
# delimiter = "\t"
ctf_file = 'vgsales'
csv_file = 'vgsales.csv'
delimiter=","

attempts = 1
ctf_function = lambda x : x
csv_function = try_conversion


def test_columns_ctf(ctf_file, function = lambda x : x):
    '''
    This will run on a given ctf file and return an array of n values each corresponding to the time needed to access n columns. It will run function on each item in each column/row.
    '''

    # get ctf access times
    ctf_times = []

    open_start = time.time()
    ctf_reader = reader(ctf_file)
    open_end = time.time()
    open_time = open_end - open_start
    for i in range(0, len(ctf_reader.columns) + 1):
        start = time.time()
        for col in ctf_reader.columns[0:i]:
            col_name = col.index_name
            for item in ctf_reader[col_name]:
                function(item)
        end = time.time()
        ctf_times.append(end-start + open_time)
        print(str(end-start + open_time) + "\n")
    return ctf_times


def test_columns_csv(csv_file, function = lambda x : x):
    '''
    This will run on a given csv file and return an array of n values each corresponding to the time needed to access n columns. It will run function on each item in each column/row.
    '''
    # get csv times
    row_len = 0
    csv_times = []
    with open(csv_file) as csv_object:
        reader = csv.reader(csv_object, delimiter=delimiter)
        x = iter(reader)
        row_len = len(next(x))

    # Runs increasingly to test columns
    for columns_to_test in range(1, row_len+1):
        start = time.time()
        with open(csv_file) as csv_object:
            reader = csv.reader(csv_object)
            # Runs on each row from the file
            for row in reader:
                # Loops through n times to test each row item and execute function on them
                for index in range(0,columns_to_test):
                    try:
                        row_item = row[index]
                        # Logic for converting first row to int
                        function(row_item)
                    except:
                         pass
        end = time.time()
        csv_times.append(end-start)
        print(str(end-start) + "\n")
    return csv_times

def print_lines(dict_of_lines):
    '''
    Accepts a dict of lines and graphs them using key as the label and value as the array of time values
    '''
    # Get the total number of rows for the header
    with open(csv_file) as f:
        total_rows = sum(1 for line in f)

    # Plot the times figure
    fig = plt.figure()
    # Setup labels
    plt.title(str(total_rows) + " rows of data accessed")
    plt.xlabel("Columns accessed")
    plt.ylabel("Average time for " + str(attempts) + " attempts")
    for key in dict_of_lines:
        # Sets the x values to be 1 based rather than 0 based
        xticks = list(range(1,len(dict_of_lines[key])+1))
        plt.xticks(xticks)
        plt.plot(xticks,dict_of_lines[key], label=key)
    plt.legend()
    fig.savefig('csv_ctf_access_times.png')

def average_attempts_array(attempts_array):
    '''
    Takes a two dimensional array of attempts and returns a one dimensional array with the averages
    '''
    average_array = []
    length_of_attempt = len(attempts_array[0])
    for index in range(0, length_of_attempt -1 ):
        average = 0
        for attempt in attempts_array:
            average += attempt[index]
        average_array.append(average / length_of_attempt)
    return average_array

def get_average_times():
    '''
    Runs n attemps and returns a dictionary containing the averages for ctf and csv
    '''
    ctf_attempts = []
    for attempt in range(0, attempts):
        ctf_attempts.append(test_columns_ctf(ctf_file, ctf_function))

    csv_attempts = []
    for attempt in range(0, attempts):
        csv_attempts.append(test_columns_csv(csv_file, csv_function))

    times_dict = {
        'ctf': average_attempts_array(ctf_attempts),
        'csv': average_attempts_array(csv_attempts),
    }
    return times_dict

# Runs the logic
print_lines(get_average_times())

