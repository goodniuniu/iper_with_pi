import requests

files = {'file': open('result.json', 'rb')}
response = requests.post("http://服务器IP地址:5000/upload", files=files)
print(response.text)
