import requests as req
import json


# Get some candle data for EUR/USD
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


# Create a user
headers = {'Content-Type': 'application/json'}
data = {'username': 'abc123', 'first_name': 'Billy', 'last_name': 'Bob', 'password': 'a', 'subscription_type': 'Premium'}
resp = req.post('http://localhost:8080/createUser', headers=headers, data=data)

if resp.status_code != 404:
        user_id = json.loads(resp.text)
        print(user_id)

else:
        print(resp.text)


# Create the same user and make sure we get an error message
headers = {'Content-Type': 'application/json'}
data = {'username': 'abc123', 'first_name': 'Billy', 'last_name': 'Bob', 'password': 'a', 'subscription_type': 'Premium'}
resp = req.post('http://localhost:8080/createUser', headers=headers, data=data)

if resp.status_code != 404:
        user_id = json.loads(resp.text)
        print(user_id)

else:
        print(resp.text)


# Login and check the user id
headers = {'Content-Type': 'application/json'}
data = {'username': 'abc123', 'password': 'a'}
resp = req.post('http://localhost:8080/login', headers=headers, data=data)

if resp.status_code != 404:
        user_id_2 = json.loads(resp.text)
        print(user_id_2 == user_id)

else:
        print(resp.text)


# Get monthly bill
headers = {'Content-Type': 'application/json'}
data = {'user_id': user_id}
resp = req.get('http://localhost:8080/getMonthlyBill', headers=headers, data=data)

if resp.status_code != 404:
        bill = json.loads(resp.text)
        print(bill)

else:
        print(resp.text)


# Get the amount of pairs followed left
headers = {'Content-Type': 'application/json'}
data = {'user_id': user_id}
resp = req.get('http://localhost:8080/getFollowedPairsLeft', headers=headers, data=data)

if resp.status_code != 404:
        pairs_left = json.loads(resp.text)
        print(pairs_left)

else:
        print(resp.text)


# Change to the basic subscription
headers = {'Content-Type': 'application/json'}
data = {'user_id': user_id, 'subscription_type': 'Basic'}
resp = req.post('http://localhost:8080/updateSubscription', headers=headers, data=data)

if resp.status_code == 404:
        print(resp.text)


# Check to see if the monthly bill changed
headers = {'Content-Type': 'application/json'}
data = {'user_id': user_id}
resp = req.get('http://localhost:8080/getMonthlyBill', headers=headers, data=data)

if resp.status_code != 404:
        bill = json.loads(resp.text)
        print(bill)

else:
        print(resp.text)


# Check to see if the pairs followed left changed
headers = {'Content-Type': 'application/json'}
data = {'user_id': user_id}
resp = req.get('http://localhost:8080/getFollowedPairsLeft', headers=headers, data=data)

if resp.status_code != 404:
        pairs_left = json.loads(resp.text)
        print(pairs_left)

else:
        print(resp.text)


# Follow a pair
headers = {'Content-Type': 'application/json'}
data = {'user_id': user_id, 'currency_pair_name': 'EUR/USD'}
resp = req.post('http://localhost:8080/updatePairsFollowed', headers=headers, data=data)

if resp.status_code == 404:
        print(resp.text)


# Check to see if the pairs followed left changed
headers = {'Content-Type': 'application/json'}
data = {'user_id': user_id}
resp = req.get('http://localhost:8080/getFollowedPairsLeft', headers=headers, data=data)

if resp.status_code != 404:
        pairs_left = json.loads(resp.text)
        print(pairs_left)

else:
        print(resp.text)


# Look at the followed pairs
headers = {'Content-Type': 'application/json'}
data = {'user_id': user_id}
resp = req.get('http://localhost:8080/getPairsFollowed', headers=headers, data=data)

if resp.status_code != 404:
        pairs_followed = json.loads(resp.text)
        print(pairs_followed)

else:
        print(resp.text)


