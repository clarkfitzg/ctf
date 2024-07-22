import os, json
from .column import Column
from .file_management import list_files, get_file_name

METASUFFIX='-metadata'
META_TYPE = "json"
COLUMNFILETYPE='txt'
            
def write(datasetName, location):
    colCounter = 0
    #TODO: check if legit dataset
    dataLoc = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/'+datasetName+'.csv'
    dataset = pd.read_csv(dataLoc)
    tableArray = []
    colArray = []
    for colName, col in dataset.items():
        colArray.append({'url': colName, 'titles': colName, 'datatype': str(dataset.dtypes[colName].name)})
        with open(colName+'.'+COLUMNFILETYPE, 'w') as colWrite:
            for value in col:
                colWrite.write(str(value)+"\n")
    tableArray.append({'url':[datasetName+'.csv'], 'tableSchema':{'columns':colArray}})
    jsonDictionary = { '@context': CONTEXT, 'tables':tableArray}
    with open(datasetName+METASUFFIX+'.'+META_TYPE, 'w') as file:
        json.dump(jsonDictionary, file, ensure_ascii=False, indent=2)