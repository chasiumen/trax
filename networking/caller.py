#!/usr/bin/python
import neutron
import keystone

##### COLOR #####
class colors:
    GREEN='\033[1;32m'
    BLUE='\033[1;34m'
    YELLOW='\033[1;33m'
    RED='\033[0;31m'
    WHITE='\033[1;37m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


#### VARIABLES ####
#Assume tenants name is same as username
#user='chasiumen'
#passwd='agumion\$0822'
#mail='morinor@devtrax.com'
user='umi'
passwd='agumion\$0822'
mail='umi@devtrax.com'



#### Keystone ####
#   1. Create user TENANT
#   2. Create user ACCOUNT
#   3. Assign user ROLE

print '==='*10 + ' CREATE USER AND TENANT ' + '==='*10
#Create an instance
keystone = keystone.Keystone(user, passwd, mail)

#get user-list
keystone.get_user()

#Create tenant
keystone.add_tenant()
#Create user
keystone.add_user()
#Assign role
keystone.add_role()


####KEYSTONE DELETE####
print '==='*10 + ' DELETE USER AND TENANT ' + '==='*10
#Delete Tenant
keystone.del_tenant()
#Delete user
keystone.del_user()



print '==='*10 + ' CREATE NETWORK AND ROUTER ' + '==='*10 
#### Neutron ####
#Create an instance
neutron = neutron.Net(user, passwd, keystone.KeyCmd)
#Create router
neutron.router("r1")
neutron.add_network()

#delete
print '==='*10 + ' DELETE NETWORK AND ROUTER ' + '==='*10
neutron.delete_network()
neutron.delete_router()
