import csv
import sys
import os
from ..ctf.column_text_format import reader

x = reader.Reader("file")

x.stream_convert_csv_to_ctf(sys.stdin,os.getcwd(), "pracDir")
