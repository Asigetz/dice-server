import requests
import threading

results = []
threads = []


def get_request(throw_number):
    pay_load = {'app': 'asaf', 'throw': throw_number}
    r = requests.get('http://localhost:8875', params=pay_load)
    results.append(r.content)


for i in range(3):
    t = threading.Thread(target=get_request, args=(i,))
    threads.append(t)
    t.start()


print(results)


