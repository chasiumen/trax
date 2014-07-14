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
#curl -i 'http://69.43.73.229:5000/v2.0/tokens' -X POST -H "Content-Type: application/json" -H "Accept: application/json"   -d '{"auth": {"tenantName": "admin", "passwordCredentials": {"username": "admin", "password": "548295a7ebf749b74d42"}}}'

##VARIABLES
#Openstack API base url
#base_url = 'http://controller.devtrax.biz:35357/v2.0'
token_url ='http://controller.devtrax.biz:5000/v2.0/tokens'

print 'Access to Horizon'
url = token_url




#Create request data
#set headers
headers={'Content-Type': 'application/json'}
#input data   data = {'key1': 'value1', 'key2': 'value2'} 
payload={'auth': {'tenantName': 'admin', 'passwordCredentials': {'username': 'admin', 'password': '548295a7ebf749b74d42'}}}



#create openstack instance
a = api.openstack_api('test')
#GET
a.get(url)
#POST
a.send(token_url, payload, headers)

