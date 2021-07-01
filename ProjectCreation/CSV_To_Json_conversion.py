import json
import csv
import requests
import openpyxl
'''
with open("C:\\Users\\karti\\PycharmProjects\\PythonStudio\\Csvfile.csv","r") as f:
    read_file=csv.reader(f)
    next(read_file)
    data={"names":[]}
    for row in read_file:
        #print(row)
        data["names"].append({"firstname":row[0], "lastname":row[1]})


with open("C:\\Users\\karti\\PycharmProjects\\PythonStudio\\Jsonfile.json","w") as f:
     json.dump(data,f,indent=4)

'''

with open("/Files_/Demoapi.csv", "r") as f:
    read_file=csv.reader(f)
    next(read_file)
    data=[]
    for row in read_file:
        #print(row)
        data.append({"name":row[0], "job":row[1]})


with open("/Files_/DemoJsonfile.json", "w") as f:
     json.dump(data,f,indent=4)

file_name= "/Files_/DemoJsonfile.json"
f1=open(file_name, 'r')
jsondata=json.load(f1)
print(jsondata)

for i in jsondata:
    print(i)



#response=requests.post("https://reqres.in/api/users",data=open(file_name,'rb'))
    response=requests.post("https://reqres.in/api/users",data=i)
    print(response.status_code)
    print(response.json())

''''
with open("C:\\Users\\karti\\PycharmProjects\\PythonStudio\\Canvascontact.csv","r") as f:
    read_file=csv.reader(f)
    next(read_file)
    data=[]
    for row in read_file:
        #print(row)
        data.append({"batch_id":row[0], "company_code":row[1],"designation":row[2],"email":row[3],"first_name":row[4],"last_name":row[5],"start_date":row[6],"end_date":row[7],"tel_no":row[8]})


with open("C:\\Users\\karti\\PycharmProjects\\PythonStudio\\CanvasJsonfile.json","w") as f:
     json.dump(data,f,indent=4)
'''