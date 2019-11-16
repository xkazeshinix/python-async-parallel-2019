import time

import requests

url = 'http://localhost:5001/compute?a=1&b=1'

st = time.time()
MX = 100
cnt = 0
for _ in range(MX):
    r = requests.get(url)
    cnt += 1
en = time.time()
elapsed_seconds = en-st
print(f'time: {elapsed_seconds}; rps: {MX / elapsed_seconds}')
# print(r.json())