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
user='chasiumen'
passwd='agumion\$0822'
mail='morinor@devtrax.com'


#### Keystone ####
#   1. Create user TENANT
#   2. Create user ACCOUNT
#   3. Assign user ROLE

#Create an instance
keystone = keystone.Keystone(user, passwd, mail)

#Create tenant
keystone.add_tenant()
#Create user
keystone.add_user()
#Assign role
keystone.add_role()


#### Neutron ####

#Create an instance
neutron = neutron.Net(user, passwd)

#Create router
neutron.router("test_router")
neutron.add_network()


#execute a command
#a.exe('ls -al ./')
#a.router(user)
#b.add_tenant(user)



#output
#print dir(a)
#print a.output
