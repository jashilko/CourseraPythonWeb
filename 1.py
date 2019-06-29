import requests
import json

payload = {"key1": "value1", "key2": "value2"}
url = 'http://httpbin.org/post'
r = requests.get('http://httpbin.org/get', payload)
#print(r.text)
r = requests.put('http://httpbin.org/put', data={"key": "value"})
r = requests.post(url, data=json.dumps({"key": "value"}))
r = requests.post(url, json={"key": "value"})
files = {"file":
             ("test.txt",
              open("test.txt",
                   "rb"))}
r = requests.post(url, files=files)
headers = {"user-agent": "my-app/0.0.1"}
r = requests.get('http://httpbin.org/get', headers=headers)

#Response
r = requests.get('http://httpbin.org/get')
# print(type(r.text), r.text)
# print(type(r.content), r.content)
# print(type(r.json()), r.json)
# print(r.status_code)
# print(r.status_code == requests.codes.ok)

# bad_r = requests.get('http://httpbin.org/status/404')
# print(bad_r.status_code)
# bad_r.raise_for_status()

#Загололовки
# print(r.headers)

# Redirect and history
# r = requests.get("http://github.com")
# print(r.url)
# print(r.status_code)
# print(r.history)

# r = requests.get("http://github.com", allow_redirects=False)
# print(r.url)
# print(r.status_code)
# print(r.history)


#Cookies
# url = 'http://httpbin.org/cookies'
# cookies = dict(cookie_are = 'working')
# r = requests.get(url, cookies=cookies)
# print(r.text)

# Session Objects\n",
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')
print(s.cookies)
print(r.text)

