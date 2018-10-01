import httplib, urllib

params = urllib.urlencode({'app': 'asaf', 'throw': 1})
headers = {"Content-type": "application/json", "Accept": "application/json"}
conn = httplib.HTTPConnection('localhost', 8875)
conn.request("POST", "/cgi-bin/query", params, headers)
response = conn.getresponse()
print response.status, response.reason

doc = conn.getresponse().read()
print doc
data = response.read()
conn.close()
