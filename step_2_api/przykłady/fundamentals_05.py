import datetime

import requests as r

url = "http://localhost:8080"
person = {"first_name": "Ildefons", "last_name": "Gałczyński"}
response = r.post(f"{url}/human/", json=person)

print(response.json())
print(response.status_code)

url = "http://localhost:8080/get_all_people_sliced?from_number=1000&to_number=1004"
response = r.get(url)
assert response.status_code == 200

print(response.json())
