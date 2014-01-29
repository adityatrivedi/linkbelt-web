#!/usr/bin/env python
import json
import os
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
	
	# set http://google.com as default URL to shorten
	# get long url from user
	long_url = request.args.get('url', 'http://google.com')
	# set goo.gl as default service
	# get service type from user
	service = request.args.get('service', 1, type=int)
	short_url = ''
	# check service type
	if service == 1:
		# goo.gl service
		request_url = 'https://www.googleapis.com/urlshortener/v1/url'
		# set arguments to the POST request
		payload = {'longUrl': long_url}
		# set the content-type
		headers = {'content-type': 'application/json'}
		# build the POST request
		r = requests.post(request_url, data=json.dumps(payload), headers=headers)
		# extract short url from json
		short_url = r.json()['id']
	elif service == 2:
		# bit.ly service
		# set login and API key
		BITLY_LOGIN = os.environ.get('BITLY_LOGIN')
		BITLY_API_KEY = os.environ.get('BITLY_API_KEY')
		# set request url
		request_url = 'http://api.bitly.com/v3/shorten'
		# set arguments to get request
		payload = {'login':BITLY_LOGIN, 'apiKey':BITLY_API_KEY, 'longUrl':long_url, 'format':'json'}
		# building request
		r = requests.get(request_url, params=payload)
		# extract short url from json
		short_url = r.json()['data']['url']
	else:
		# tinyurl service
		# set request url
		request_url = 'http://tinyurl.com/api-create.php'
		# set arguments to get request
		payload = {'url': long_url}
		# build request
		r = requests.get(request_url, params=payload)
		# extract short url
		short_url = r.text

	# pass long_url and short_url to index.html
	return render_template('index.html', long_url=long_url, short_url=short_url)

if __name__ == '__main__':
	app.run()
