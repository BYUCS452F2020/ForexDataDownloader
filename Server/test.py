import requests as req
import json

headers = {'Content-Type': 'application/json'}
data = {'currency_pair': 'EUR_USD', 'time_frame_granularity': 'H1',
        'from_time': '2020-10-05 00:00:00', 'to_time': '2020-10-06 00:00:00'}
resp = req.get('http://localhost:8080/getHistoricalData', headers=headers, data=data)

if resp.status_code != 404:
        candles = json.loads(resp.text)
        candles = json.dumps(candles, indent=4)
        print(candles)

else:
        print(resp.text)

