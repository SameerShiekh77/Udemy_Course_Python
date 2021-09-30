# HTTP REQUEST
'''
200 OK
403 FORBIDDEN
404 NOT FOUND
'''
import requests
r = requests.get("https://google.com")
print(r.status_code)
print("Headers:", r.headers)
print("\n", r.text)
print(r.headers['Date'])