import datetime

import requests as r

url = "http://localhost:8080/query_params?first_name=Olga&last_name=Patyna"
response = r.get(url)
assert response.status_code == 200

print(response.json())