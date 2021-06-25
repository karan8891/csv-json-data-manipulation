# Importing required libraries

import csv, json
import pandas as pd
from glob import glob

# match and sort results with glob

merged_csv = sorted(glob('{path-to-courses-file}' '{path-to-students-file}' '{path-to-tests-file}' '{path-to-marks-file}'
'{path-to-output-file}'))

# concatenation of all files

csv_File = pd.concat((pd.read_csv(file).assign(filename = file)
	for filw in merged_csv), ignore_index = True)

# storing values in variables

json_File = "output.json"

# Reading the target file and adding data to a dictionary

data = {}

# Removing Byte Order Mark by encoding specification

with open(csv_File, encoding='utf-8-sig') as csv_Object:
	csv_Reader = csv.DictReader(csv_Object)
	for csv_Row in csv_Reader:
		id = csv_Row["id"]
		data[id] = csv_Row
print(data)

# Writing data into a json file

with open(json_File, "w") as json_Object:

# indent set to 4 for readability

	json_Object.write(json.dumps(data, indent = 4))
