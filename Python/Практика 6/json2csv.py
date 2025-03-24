import json  

import csv   
import sys   

import os    


json_file = sys.argv[1]


try:
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

except FileNotFoundError:
    print(f"Файл не найден: {json_file}")

    sys.exit(1)

except json.JSONDecodeError:
    print(f"Некорректный JSON-файл: {json_file}")
    sys.exit(1)

key= list(data.keys())[0]

records = data[key]

if not records:

    print("В JSON-файле нет записей.")
    sys.exit(1)

csv_file  = os.path.splitext(json_file)[0] + "__" + key + ".csv"

headers =records[0].keys()

with open(csv_file, 'w', newline = '', encoding = 'utf-8') as f:

    writer= csv.DictWriter(f, fieldnames=headers)
    
    writer.writeheader()  

    for record in records:

        writer.writerow(record)  

print(f"CSV-файл успешно создан: {csv_file}")