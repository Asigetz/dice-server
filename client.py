import requests
payLoad = {'app': 'asaf', 'throw': 1}
r = requests.get('http://localhost:8875', params = payLoad)
print (r.content);
