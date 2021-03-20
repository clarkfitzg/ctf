import csv
import sys

# simply prints out the global sales of a video game from a csv file streamed in
# also how would I skip the header? I had issues with this and couldn't find any 
# good answers online

for row in csv.reader(iter(sys.stdin.readline,'')):

    
    print(row[10])

