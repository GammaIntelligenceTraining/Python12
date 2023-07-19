import json
#
# data = '''{
#   "people": [
#     {
#       "name": "Jack Sumers",
#       "phone": "555-555-555",
#       "emails": ["jack.sumers@example.com", "jacksumers@work-place.com"],
#       "has_licence": false,
#       "salary": 1500
#     },
#     {
#       "name": "Mary Smith",
#       "phone": "777-777-777",
#       "emails": null,
#       "has_licence": true,
#       "salary": 1700
#     },
#     {
#       "name": "Steven Cooke",
#       "phone": null,
#       "emails": "stevencooke@example.com",
#       "has_licence": true,
#       "salary": 2500
#     }
#   ]
# }'''
#
# json_data = json.loads(data)
# del json_data['people'][1]['name']
#
# new_json = json.dumps(json_data, indent=4)
# print(new_json)
# print(type(new_json))

with open('data.json', 'r', encoding='UTF8') as file:
    data = json.load(file)
    print(data)
    print(type(data))


for person in data['people']:
    if person['has_licence'] == False:
        del person['has_licence']

with open('new_data.json', 'w', encoding='UTF8') as file:
    json.dump(data, file, indent=2)
