from column_text_format import reader
import time

ctf_file = '/home/ec2-user/GDELT'
csv_file = '/mnt/extra/2018.csv'
delimiter = "\t"

ctf_reader = reader(ctf_file)

def time_col(n):
    start = time.time()
    for col in ctf_reader.columns[0:n]:
        col_name = col.index_name
        for item in ctf_reader[col_name]:
            pass
    end = time.time()
    return end-start

try:
    for i in range(1,62):
        print(str(time_col(i)), flush=True)
except:
    print("ERROR")

print("End")