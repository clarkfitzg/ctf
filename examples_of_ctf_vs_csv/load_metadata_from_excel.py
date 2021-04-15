import xlrd
import json

with open(metadata_file) as file:
    json_data = json.load(file)
default_column = json_data["tableSchema"]["columnFiles"][1]

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