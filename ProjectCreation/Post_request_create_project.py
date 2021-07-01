import openpyxl
import requests
import json
import random
import time


package_item_file_path="C:\\Users\\karti\\PycharmProjects\\PythonStudio\\Files_\\Package_item_data_in_ison.json"
package_item_file=open(package_item_file_path,'r')
package_item_file_json=json.load(package_item_file)

oath_token='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXV0aC5hcGkuc3BlYy5sb3ZldGhhdC5kZXNpZ25cL2FwaVwvbG9naW4iLCJpYXQiOjE2MjUwNjA3NDMsImV4cCI6MTYyNTIzMzU0MywibmJmIjoxNjI1MDYwNzQzLCJqdGkiOiJHTUppYVg3OGZXdFJRdk00Iiwic3ViIjoxMDcsInBydiI6ImY4MzhiOTUwOWFhZjk0YzMzODZmNjc5Zjg5MjljZGM3NjdjNzBmMmYiLCJ1c2VyX2NhY2hlX2tleSI6ImV5SnBkaUk2SWxsR1NsSlRhRlphWW1JeGFXVjBaMGhEVDBacGFtYzlQU0lzSW5aaGJIVmxJam9pVDJwT2FtazFlRzlZUm05V05VMW5aelpGZW01UGExTlZia3RqVUdoTGJWd3ZkMEYxTlhBeU1ETjZXRmhTUzF3dlkySTBlWFIwZUdweWJteFlNMHBIVlZsdElpd2liV0ZqSWpvaU5UUmhZalpqWXpKallqUXdOak5sWTJJMU1ESmxOemhrTkRKa05EQmtNems0WWpVMVlUWTVaREkwWVRjNU0yWXdOV1JqTVRrelkyRmpZVEJqWVRFMk5pSjkiLCJjb21wYW55X2FjY291bnRfY29kZSI6ImV5SnBkaUk2SWpNMVZuQnFTREJRZURGMGVHWjRVMEpyT1dSemNVRTlQU0lzSW5aaGJIVmxJam9pVDJ4dWIzQkhPVFZ0VG5OVE5EQTVSbkpsVjFWR1l6UTFaWEF5V2tWcFJFUkpjblYwWjFWQ2Qxb3liejBpTENKdFlXTWlPaUptT0RSbVlUQTFaRGhsTTJKallUQTJNalF3TWpsbE56RTJPRFUxTmprMVpETTBaVGsyTkRRMFlUWTRabUptTTJVMU1USTFNbVl5TUdGbU4yRmtOVGt5SW4wPSJ9.aIauOaiM5ua3TrMlFykqjmLYHyAqgd3rNVfCEQxYQBs'
headers = {'Authorization': oath_token, 'Content-Type': 'application/json', 'Accept': 'text/plain'}
sequence="1743353dffsdnvbvcf234567anvdd"

count=1
#time when while loop started
t1=time.perf_counter()
while count != 0:

   project_name="Python-Automation-"+''.join((random.choice(sequence)) for x in range(5))
   payload={
       "batch_id": "66a94bebdde56d4dadda569dcc9d28fd96d3",
       "company_name": "",
       "company_code": "28-lightbulbs",
       "name": project_name,
       "reference_no": "",
       "external_url": "",
       "description": "",
       "address": "607 Uniestate millennium tower, Dubai silicon oasis\n607",
       "city_name": "Dubai Silicon Oasis",
       "state": "Dubai",
       "zip_code": "99009900",
       "country_code": "AF",
       "start_date": "20-06-2021" ,
       "end_date": "",
       "estimated_duration": 0,
       "estimated_value": "",
       "exchange_rate": "",
       "estimated_value_currency_code": "GBP",
       "responsible_code": "ER527",
       "custom_data": [
           {
               "code": "project-vat",
               "type": "currency"
           }
       ],
       "groups": "",
       "project_types": [
           "construction-1"
       ],
       "tags": []
   }
   data=json.dumps(payload,indent=2)
   print(data)
   response=requests.post("https://designer.api.spec.lovethat.design/api/designer/v1.0/projects/",headers=headers, data=data)
   #api response time
   print(response.elapsed.total_seconds())
   print("######Project Creation Status code is###### ",response.status_code)
   print("Project Response body is ",response.json())
   response1=response.json()
   #print(response1)
   project_code=response1['data']['code']

   package_count=1
   while package_count!=0:
      package_name = "Package-"+''.join((random.choice(sequence)) for x in range(4))
      package_payload={
      "batch_id": "010eb893f3d53f4b7ef8617f302468e52d00",
      "code": "",
      "maps": [],
      "name": package_name,
      "project_code": project_code
        }
      package_data=json.dumps(package_payload)
      package_response = requests.post("https://designer.api.spec.lovethat.design/api/designer/v1.0/projects/packages", headers=headers,
                               data=package_data)
      print("*******Status code of package creation is****** ", package_response.status_code)
      print("Response body of package is ", package_response.json())
      package_item_count = 1
      while package_item_count != 0:
            package_item_code ="Code-" +''.join((random.choice(sequence)) for x in range(4))
            package_item_name = "Name-" + ''.join((random.choice(sequence)) for x in range(4))

            package_item_file_json['package_item']["package_code"]= package_name
            package_item_file_json['package_item']["product_record_code"]= package_item_code
            package_item_file_json['package_item']["name"]= package_item_name
            package_item_data = json.dumps(package_item_file_json)
            package_url=f"https://designer.api.spec.lovethat.design/api/designer/v1.0/projects/packages/{package_name}/package-items?force=false&view=sections"
            print(package_url)
            package_item_response = requests.post(url=package_url, headers=headers, data=package_item_data)
            print("@@@@@@@Status code of package item creation is@@@@@@@ ", package_item_response.status_code)
            print("Response body of package item is ", package_item_response.json())
            package_item_count=package_item_count-1
      package_count=package_count-1
   count=count-1
#time when while loop ended
t2=time.perf_counter()
print("Total time taken to execute the while loop ",t2-t1)













