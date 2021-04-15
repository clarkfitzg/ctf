#import xlrd
import json
import csv 

with open("template_ctf.json") as file:
    json_data = json.load(file)
    
default_column = json_data["tableSchema"]["columnFiles"][0]

print(default_column) 

with open("GDELT_2.0_Events_Column_Labels_Header_Row_Sep2016.csv") as csv_file:
    next(csv_file) #skip the first line since it is the header
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row[1]) 


"""
book = xlrd.open_workbook("myfile.xls")
sh = book.sheet_by_index(0)


for(i in range(1,61)):
    new_column = default_column
    new_column["url"] = "column" + str(i)
    new_column["datatype"]["base"] = sh.cell_value(2, i)
    json_data["tableSchema"]["columnFiles"].append(new_column)

out_json = json.dumps(json_data, indent=4, sort_keys=True)

with open("newFile") as file:
    file.write(out_json)

"""
