import json

with open('2.json','r') as f:
    content =f.read()  

json_str ='[' + content + ']'

data= json.loads(json_str)

formatted_json =json.dumps(data, indent=4)

with open('formatted_users.json', 'w') as f:

    f.write(formatted_json)

user_phones = {user['name']:user['phoneNumber'] for user in data}

print(user_phones)