#!/usr/bin/env python
import json
import requests

# take input from the user
input = raw_input('Go ahead and enter a long URL you want to shorten: ')
# url to goo.gl service
url = 'https://www.googleapis.com/urlshortener/v1/url'
# arguments to the POST request
payload = {'longUrl': input}
# setting the content-type
headers = {'content-type': 'application/json'}
# building the POST request
r = requests.post(url, data=json.dumps(payload), headers=headers)
# convert data to json
data = r.json()
# print the short url to the terminal
print(data['id'])