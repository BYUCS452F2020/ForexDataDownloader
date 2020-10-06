import requests as req

headers = {'Content-Type': 'application/json'}
data = {'currency_pair': 'EUR_USD', 'time_frame_granularity': 'H1',
        'from_time': '2020-09-15 00:00:00', 'to_time': '2020-09-15 12:00:00'}
resp = req.get('http://localhost:8080/getHistoricalData', headers=headers, data=data)

print(resp.text)
