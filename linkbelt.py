#!/usr/bin/env python
import json
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
	long_url = request.args.get('url', 'http://google.com')
	# url to goo.gl service
	url = 'https://www.googleapis.com/urlshortener/v1/url'
	# arguments to the POST request
	payload = {'longUrl': long_url}
	# setting the content-type
	headers = {'content-type': 'application/json'}
	# building the POST request
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	# convert data to json
	data = r.json()
	# pass long_url and short_url to index.html
	return render_template('index.html', long_url=long_url, short_url=data['id'])

if __name__ == '__main__':
	app.run()