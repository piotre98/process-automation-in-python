import datetime

import requests as r

url = "http://localhost:8080/ok"
response = r.get(url)
assert response.status_code == 200
"""
{
  "basicInformation": "This is GET example for status code 200",
  "responseInformation": {
    "shortDescription": "OK",
    "longDescription": "The request has succeeded"
  },
  "timestamp": "2022-06-24 11:25:09.604893"
}
"""

body = response.json() # to jest dict
print(body)

print(body['basicInformation'])
print(body['responseInformation']['longDescription'])
print(body['timestamp'])

# print(body['timestamp'] < datetime.datetime.now())
print(datetime.datetime.strptime(body['timestamp'], "%Y-%m-%d %H:%M:%S.%f") < datetime.datetime.now())

delta = datetime.timedelta(minutes=-1)
print(datetime.datetime.strptime(body['timestamp'], "%Y-%m-%d %H:%M:%S.%f") > datetime.datetime.now() + delta)
