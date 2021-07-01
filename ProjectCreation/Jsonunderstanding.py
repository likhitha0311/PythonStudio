import json



people_json_string='''
    {
    "people_string":[{"name":"John Smith",
"emails":["john@mail.com","john@bogus.com"],
"phone":"1234455",
"has_license":true
},
{"name":"JaneDoa",
"emails":["john@mail.com","john@bogus.com"],
"phone":"1234-6777-455",
"has_license":false
}]
}
'''
print(people_json_string)
#Convert valid json string to python object or python dictionary,you cannot convert json object to python dictionary since it throws type error, by default json object=python dictionary
data=json.loads(people_json_string)
print (data)

print(type(data))
print(data['people_string'][0]['phone'])
for person in (data['people_string']):
    print(person['name'])

for person in (data['people_string']):
    del person['phone']

print(data)
#Convert python object or python dictionary to json string
json_string=json.dumps(data, indent=2, sort_keys=True)
print(json_string)
print(type(json_string))

with open('C:\\Users\\karti\\PycharmProjects\\PythonStudio\\Files_\\Jsonfile.json') as f:
    data1=json.load(f)
    print(data1)
    print(data1['names'][0]['firstname'])

for names1 in data1['names']:
    print(names1['firstname'])
    del (names1['lastname'])

print(data1)
#Convert python object or python dictionary to json string
json_d=json.dumps(data1)
print(json_d)
#Convert python object or python dictionary to valid json file/document
with open('new_json.json','w',) as f:
    json_file_data=json.dump(data1,f,indent=2)
