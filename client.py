import requests
import threading
import json

threads = []
results_round = []
results = []


def get_request(throw_number):
    pay_load = {'app': 'asaf', 'throw': throw_number}
    r = requests.get('http://localhost:8875', params=pay_load)
    resp_dict = json.loads(r.content)
    results_round.append(resp_dict['result'])


def throw_round(j):
    for k in range(j, j + 5, 1):
        t = threading.Thread(target=get_request, args=(k,))
        threads.append(t)
        t.start()
        t.join()
    return results_round;


for i in range(0, 50, 5):
    throw_round(i)
    results.append(results_round)
    results_round = []

print(results)
