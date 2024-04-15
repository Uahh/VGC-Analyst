import csv 
import json
import time

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          

scv_list = ['pokemon.csv', 'pokemon_types.csv', 'moves.csv', 'types.csv', 'pokemon_stats.csv']
scv_list = ['pokemon_stats.csv']

for csv_file in scv_list:
    csvFilePath = './data/csv_raw/' + csv_file
    jsonFilePath = './data/' + csv_file[:-4] + '.json'

    start = time.perf_counter()
    csv_to_json(csvFilePath, jsonFilePath)
    finish = time.perf_counter()

types = {}
result = {}
with open('./data/types.json') as json_file:
    types = json.load(json_file)
    for type in types:
        result[type['id']] = type['identifier']

with open('./data/types.json', 'w', encoding='utf-8') as jsonf: 
    jsonString = json.dumps(result)
    jsonf.write(jsonString)
types = result

result = {}
with open('./data/pokemon_types.json') as json_file:
    pokemon_types = json.load(json_file)
    for pokemon_type in pokemon_types:
        if pokemon_type['pokemon_id'] not in result.keys():
            result[pokemon_type['pokemon_id']] = [types[pokemon_type['type_id']]]
        else:
            result[pokemon_type['pokemon_id']].append(types[pokemon_type['type_id']])

with open('./data/pokemon_types.json', 'w', encoding='utf-8') as jsonf: 
    jsonString = json.dumps(result)
    jsonf.write(jsonString)