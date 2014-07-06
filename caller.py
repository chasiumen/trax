#!/usr/bin/python
import api
import subprocess
import json

#
#OS_USERNAME=admin
#OS_PASSWORD=548295a7ebf749b74d42
#OS_TENANT_NAME=admin
#OS_AUTH_URL=http://controller.devtrax.biz:35357/v2.0


uname='admin'
pasword='548295a7ebf749b74d42'
tenant='admin'




#curl -i 'http://controller.devtrax.biz:5000/v2.0/tokens' -X POST -H "Content-Type: application/json" -H "Accept: application/json"  -d '{"auth": {"tenantName": "admin", "passwordCredentials": {"username": "admin", "password": "devstack"}}}'


#curl -i 'http://controller.devtrax.biz:5000/v2.0/tokens' -X POST -H "Content-Type: application/json" -H "Accept: application/json"  -d '{"auth": {"tenantName": "admin", "passwordCredentials": {"username": "admin", "password": "548295a7ebf749b74d42"}}}'


##VARIABLES
#Openstack API base url
base_url = 'http://controller.devtrax.biz:35357/v2.0'

token_url ='http://controller.devtrax.biz:5000/v2.0/tokens'


#Github repo to push
repo = 'https://github.com/chasiumen/github-api-testing.git'
#working directory
wdir = '/Users/leox/github/github-api-testing/'

#curl -i 'http://69.43.73.229:5000/v2.0/tokens' -X POST -H "Content-Type: application/json" -H "Accept: application/json"   -d '{"auth": {"tenantName": "admin", "passwordCredentials": {"username": "admin", "password": "548295a7ebf749b74d42"}}}'

##USER INPUT
print 'Access to Horizon'
url = base_url

#headers={'Accept': 'application/json'}
headers={'Content-Type': 'application/json'}
#data = {'key1': 'value1', 'key2': 'value2'} 
payload={'auth': {'tenantName': 'admin', 'passwordCredentials': {'username': 'admin', 'password': '548295a7ebf749b74d42'}}}
print payload

#print url
a = api.openstack_api('test')
a.get(url)
a.send(token_url, payload, headers)

