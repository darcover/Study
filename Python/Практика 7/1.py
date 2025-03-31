import json
from jsonschema import validate,ValidationError

with open('1_schema.json','r', encoding ='utf-8') as f:

    schema =json.load(f)

def validate_json(filename):

    with open(filename,'r', encoding ='utf-8') as f:

        data =json.load(f)
    try:
        validate(instance= data, schema =schema)

        print(f"Файл {filename} успешно прошёл валидацию.")

    except ValidationError as e:

        print(f"Ошибка валидации файла {filename}:{e.message}")

validate_json('1.json')
validate_json('1_error.json')
