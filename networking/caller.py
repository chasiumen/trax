#!/usr/bin/python
import sys, os.path


#Load modules
#keystone class
#neutron class
mPath='./lib/'
if os.path.isfile(mPath+'neutron.py') and os.path.isfile(mPath+'keystone.py'):
    sys.path.append(mPath)
    import neutron
    print "Module [neutron] added..."
    import keystone
    print "Module [keyston] added..."
    
else:
    print "Unable to load modules"
    sys.exit()



#### VARIABLES ####
#Assume tenants name is same as username
#user='chasiumen'
#passwd='agumion\$0822'
#mail='morinor@devtrax.com'
user='umi'
passwd='agumion\$0822'
mail='umi@devtrax.com'
router=user+'\'s router'
#router='r1'

#### Keystone ####
#   1. Create user TENANT
#   2. Create user ACCOUNT
#   3. Assign user ROLE

print '==='*10 + ' CREATE USER AND TENANT ' + '==='*10
#Create an instance
keystone = keystone.Keystone(user, passwd, mail)

#####KEYSTONE DELETE####
#print '==='*10 + ' DELETE USER AND TENANT ' + '==='*10
##Delete Tenant
keystone.del_tenant()
##Delete user
keystone.del_user()


#get user-list
keystone.get_user()

#Create tenant
keystone.add_tenant()
#Create user
keystone.add_user()
#Assign role
keystone.add_role()




print '==='*10 + ' CREATE NETWORK AND ROUTER ' + '==='*10 
#### Neutron ####
#Create an instance
neutron = neutron.Net(user, passwd, keystone.KeyCmd)
#Create router
neutron.router(router)
neutron.add_network()

##delete
#print '==='*10 + ' DELETE NETWORK AND ROUTER ' + '==='*10
#neutron.delete_network()
#neutron.delete_router()
