from column_text_format import reader
import time
import logging

# ctf_file = '/home/ec2-user/GDELT'
# csv_file = '/mnt/extra/2018.csv'
# delimiter = "\t"
ctf_file = 'vgsales'
csv_file = 'vgsales.csv'
delimiter=","

ctf_reader = reader(ctf_file)

logging.basicConfig(filename='app.log', filemode="a")

def time_col(n):
    start = time.time()
    for col in ctf_reader.columns[0:n]:
        col_name = col.index_name
        for item in ctf_reader[col_name]:
            pass
    end = time.time()
    return end-start

f = open("times.txt", "a")
try:
    for i in range(1,62):
        time_str = str(time_col(i))
        print(time_str, flush=True)
        f.write(time_str)
except:
    logging.error("error")

logging.error("end")