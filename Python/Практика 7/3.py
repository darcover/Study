import json

with open('3.json','r', encoding ='utf-8') as f:
    data =json.load(f)

new_invoice ={
    "id" :3,
    "total": 35.00,
    "items": [
        {
            "name": "item 4",
            "quantity": 3,
            "price": 4242.00
        },
        {
            "name": "item 5",
            "quantity": 2,
            "price": 42.00
        }]}

data['invoices'].append(new_invoice)

with open('3_updated.json','w', encoding ='utf-8') as f:

    json.dump(data, f, indent=4)
    
print("Новый файл 3_updated.json успешно создан")
