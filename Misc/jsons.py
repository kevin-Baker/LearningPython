import json
people_string = '''
{
    "people": [
        {
            "name": "John",
            "phone": "234-555-5555",
            "emails": ["Jons@gmail","Johnwork@gmail.com"],
            "has_license": false
        },
        {
            "name": "Audie",
            "phone": "234-575-5588",
            "emails": ["Audie@gmail","Audiework@gmail.com"],
            "has_license": true
        }
    ]
}
'''
data = json.loads(people_string)
for person in data['people']:
    print(person['name'])

for person in data['people']:
    del person['phone']
new_string = json.dumps(data, indent=2, separators=(". ", " = "))
print(new_string)

with open("Data.json", "w") as write_file:
    json.dump(data,write_file)

with open("Data.json", "r") as read_file:
    data = json.load(read_file)
    print(data)