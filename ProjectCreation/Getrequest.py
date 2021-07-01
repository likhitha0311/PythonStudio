import openpyxl
import requests
import json

oath_token='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvY2FudmFzLWRldi1hcGkubG92ZXRoYXQuZGVzaWduXC9hcGlcL2NhbnZhc1wvdjEuMFwvYXV0aFwvbG9naW4iLCJpYXQiOjE2MjQwOTM5OTcsImV4cCI6MTYyNDE4MDM5NywibmJmIjoxNjI0MDkzOTk3LCJqdGkiOiJBem0xTm9pRXNvdTIxV3J1Iiwic3ViIjpudWxsLCJwcnYiOiJlNDM2NDAyZGYzNTczYjgwOTRmMDhlMmI5YWZhYzAzMzA0YzFiZmIxIiwidXNlcl9jYWNoZV9rZXkiOiJleUpwZGlJNklqaHZhRXhhZFVkU2VsRnRVV3B1VlhOUVJFUnhWbmM5UFNJc0luWmhiSFZsSWpvaWFXbzRlVXRoVkhsd1JIZ3hUa05zYVV4Ukx6Vm5TVzU1VURsQ1RpdG1kVWRQTlVGek1FOUtXbUpUWjJKQmFFSnlkbTVCZWtGVFFYTllPR05xYVZsalJDSXNJbTFoWXlJNklqRXlOR001TlRKaU1EazROV0V3TURGak5EWXhObUZrWTJOak56RTVNR0ZqTW1VeFltVmxaRFUzWVRWaE5qQm1ZV1l4WmpZMU5qaGlNelEwT0dNME16Y2lmUT09In0.X-NuoSRA65SR9gsGjSpfpaNllmVYbub_s0xJleXNsnk'
headers = {'Authorization': oath_token, 'Content-Type': 'application/json', 'Accept': 'text/plain'}
#response=requests.get("https://canvas-dev-api.lovethat.design/api/canvas/v1.0/company", headers=headers)

payload={
'batch_id':'977ba86c-19db-4ad9-8a3d-14a922785aa0',
"company_code":"anischay-bilders",
"contact_tag":"",
"designation":"system analyst",
"email":"akisha@ya0hoo0mmmail.com" ,
"end_date":"null",
'first_name':'AKaisha',
'last_name':'Ahmed',
"lead_source":"fb",
"start_date":"2021-06-27 00:00:00",
"end_date":"",
"tel_no":"187786755"
}
data=json.dumps(payload)
response=requests.post("https://canvas-dev-api.lovethat.design/api/canvas/v1.0/contact", headers=headers, data=data)
print(response.status_code)
print(response.json())

