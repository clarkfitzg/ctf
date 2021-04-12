import csv
import sys
import os
import column_text_format as ctf

x = ctf.Reader("file")

x.stream_convert_csv_to_ctf(sys.stdin,os.getcwd(), "pracDir", delimiter = "\t")
