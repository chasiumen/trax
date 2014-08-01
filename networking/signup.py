#!/usr/bin/python
#caller function: create users, instances, and networks

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
mPath='./scripts/lib/'
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
    if len(sys.argv) != 4:
        print "Error: Number of command-line argeument mismatch"
        sys.exit("Useage: ./caller.py USER PASSWD EMAIL")
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
        name_r = 'r1'
        mail = sys.argv[1]+'@devtrax.com'
       

####################### KEYSTONE ############################
        print '==='*10 + ' CREATE USER AND TENANT ' + '==='*10
        #Create an instance
        keystone = keystone.Keystone(user, passwd)
        
        #get user-list
        keystone.get_user()

        #Create user account
        keystone.add_user(mail)
        
        #Create tenant
        keystone.add_tenant()
        #Create user keystone.add_user(mail)
        #Assign role
        keystone.add_role()
####################### NEUTRON ############################
        print '==='*10 + ' CREATE NETWORK AND ROUTER ' + '==='*10 
        #### Neutron ####
        #Create an instance
        neutron = neutron.Net(user, passwd, keystone.KeyCmd, name_r)
        neutron.add_router()
        neutron.add_network()
        #Create router
