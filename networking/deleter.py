#!/usr/bin/python
# deleter.py:   removes users, tenants, instances, and networks

#                           KEYSTONE
#           STEPS               |           Variables
#---------------------------------------------------------------------------|
#   1. Create Keystone instance |   username, password                      |
#   2. Create user TENANT       |           N/A                             |
#   3. Create user USER/ACCOUNT |   email                                   |
#   4. Assign user ROLE         |           N/A                             |
#                               |                                           |
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  
#                           NEUTRON                                         |
#   1. Create Neutron instance  |  username, password, KeyCmd, router_name  |
#   2. Create router            |           N/A                             |
#   3. Create network           |           N/A                             |
#
#

    
import sys, os.path
#load additonal modules
mPath='./lib/'
if os.path.isfile(mPath+'neutron.py') and os.path.isfile(mPath+'keystone.py') is False:
    sys.exit("Error: Unable to load modules")
else:
    sys.path.append(mPath)
    import neutron
    print "Module [neutron] added..."
    import keystone
    print "Module [keyston] added..."

#Check number of argeument
#username, passwd, email, router_name
    if len(sys.argv) != 5:
        print "Error: Number of command-line argeument mismatch"
        sys.exit("Useage: ./caller.py USER PASSWD EMAIL ROUTER")
    else:
        #### VARIABLES ####
        #Assume tenants name is same as username
        #user='umi'
        #passwd='agumion\$0822'
        #mail='umi@devtrax.com'
        #router='r1'
        user = sys.argv[1]
        passwd = sys.argv[2]
#        mail = sys.arg[3]
        router = sys.argv[4]
        mail = sys.argv[1]+'@devtrax.com'
 
        #### Neutron ####
        print '==='*10 + ' DELETE NETWORK AND ROUTER ' + '==='*10
        #Create an instance
        neutron = neutron.Net(user, passwd, keystone.KeyCmd, router)
        neutron.delete_network()
        neutron.delete_router()
        
        
        #### Keystone ####
        #   1. Create user TENANT
        #   2. Create user ACCOUNT
        #   3. Assign user ROLE
        
        
        #####KEYSTONE DELETE####
        print '==='*10 + ' DELETE USER AND TENANT ' + '==='*10
        #Create an instance
        keystone = keystone.Keystone(user, passwd, mail)
        ##Delete Tenant
        keystone.del_tenant()
        ##Delete user
        keystone.del_user()
        
        #get user-list
        keystone.get_user()
        
        
        
