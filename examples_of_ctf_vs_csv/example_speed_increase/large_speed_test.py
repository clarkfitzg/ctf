from column_text_format import reader
import time
import logging
import csv


ctf_file = '/home/ec2-user/GDELT'
csv_file = '/mnt/extra/2018.csv'
delimiter = "\t"
# ctf_file = 'vgsales'
# csv_file = 'vgsales.csv'
# delimiter=","

# ctf_reader = reader(ctf_file)

logging.basicConfig(filename='app.log', filemode="a")

# def time_col(n):
#     start = time.time()
#     for col in ctf_reader.columns[0:n]:
#         col_name = col.index_name
#         for item in ctf_reader[col_name]:
#             pass
#     end = time.time()
#     return end-start

# f = open("times.txt", "a")
# try:
#     for i in range(1,62):
#         time_str = str(time_col(i))
#         print(time_str, flush=True)
#         f.write(time_str + "\n")
# except:
#     logging.error("error")
#     print("end")

# print("end")
# logging.error("end")

# get csv times
num_columns = 0
csv_times = []
with open(csv_file) as csv_object:
    reader = csv.reader(csv_object, delimiter=delimiter)
    x = iter(reader)
    num_columns = len(next(x))

print("began", flush=True)

# Runs increasingly to test columns
# for columns_to_test in range(0,2):
for columns_to_test in range(num_columns, num_columns + 1):
    with open(csv_file) as csv_object:
        start = time.time()
        reader = csv.reader(csv_object, delimiter=delimiter)
        # Runs on each row from the file
        for row in reader:
            # Loops through n times to test each row item and execute function on them
            for index in range(0,columns_to_test):
                try:
                    something = int(row[index])
                    # row_item = row[index]
                    # # Logic for converting first row to int
                    # function(row_item)
                except:
                    pass
        end = time.time()
        print(str(end-start) + "\n", flush=True)
# csv_times.append(end-start)