import requests
import threading
import json
import Queue

threads = []
results = []


def get_request(throw_number):
    pay_load = {'app': 'asaf', 'throw': throw_number}
    r = requests.get('http://localhost:8875', params=pay_load)
    resp_dict = json.loads(r.content)
    results.append(resp_dict['result'])

for i in range(5):
    t = threading.Thread(target=get_request, args=(i,))
    threads.append(t)
    t.start()
    t.join()

print results


