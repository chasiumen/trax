#!/usr/bin/python
import subprocess

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


######### NETWORK MANAGEMENT ########
#Class Neutron
class Net:
    def __init__(self, name, passwd):
        self.__name__ = name
        self.user = name
        self.passwd = passwd
        self.tenant = name
        self.auth_url='http://controller:35357/v2.0'
        self.cred = '--os-username=' + self.user + ' --os-password=' + self.passwd + ' --os-tenant-name=' + tenant + ' --os-auth-url=' + auth_url
        print 'Created [Net] instance successfully'
    
    #add a router
    def router(self, router):
        self.router = router
        cmd = 'neutron router-create ' + self.router + self.cred
        print colors.WHITE + cmd + colors.ENDC

        ##Create User router
        #neutron router-create [router_name]  + cred
        #neutron router-gateway-set [router_name] ext-net + cred
        
        
        cmd = 'cat /etc/resolv.conf'
        self.exe(cmd)

    #def add_network(self, url):
    #execute shell comannd
    def exe(self, cmd):
        p =subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate()
        self.output = out.rstrip()
        return self.output

#def get_tenant:
    #load admin cred
    #source /root/admin-openrc.sh
    ##export OS_USERNAME=admin
    ##export OS_PASSWORD=548295a7ebf749b74d42
    ##export OS_TENANT_NAME=admin
    ##export OS_AUTH_URL=http://controller:35357/v2.0
    #Get tenant list

######### Account Management #########
#Class Keystone
class Keystone:
    def __init__(self, name, passwd, email):
        self.name = name
        self.passwd = passwd
        self.email = email
        self.tenant = name
        self.desc = 'User Tenant'
        self.role = 'admin'
        print 'Created ' + colors.WHITE + name + colors.ENDC + '\'s ' + '[Keyston] instance successfully'

    #               ---------- CREATE FUNCTIONS ----------
    #
    #

    #CREATE TENANTS
    #keystone tenant-create --name=testuser --description="Test User Tenant"
    #
    def add_tenant(self):
        cmd ='keystone tenant-create --name=' + self.tenant + ' --description=\"' + self.desc + '\"'
        print 'CMD:'+ colors.WHITE + cmd + colors.ENDC
        print colors.RED + 'Created User account successfully' + colors.ENDC

    #CREATE USERS 
    #keystone user-create --name=chasiumen --pass=admin --email=morinor@devtrax.com
    #    
    def add_user(self):
        cmd = 'keystone user-create --name=' + self.name + ' --pass=' + self.passwd + ' --email=' + self.email
        print 'CMD:'+ colors.WHITE + cmd + colors.ENDC
        print colors.RED + 'Created User tenant successfully' + colors.ENDC

    #ADD ROLE 
    #keystone user-role-add --user=chasiumen --role=admin/member --tenant=testuser
    #    
    def add_role(self):
        cmd = 'keystone user-role-add --user=' + self.name + ' --role=' + self.role + ' --tenant=' + self.tenant
        print 'CMD:'+ colors.WHITE + cmd + colors.ENDC
        print colors.RED + 'Add ' + self.name + ' as [' + self.role + '] successfully' + colors.ENDC

    #               ---------- REMOVE FUNCTIONS ----------
    #
    #

    #DELETE TENANTS
    #keystone user-role-remove --user=chasiumen --role=_member_ --tenant=testuser
    #
    def del_tenant(self):
        cmd = ''

    #DELETE TENANTS
    #keystone tenant-delete testuser
    #
    def del_user(self):
        cmd = ''

#### VARIABLES ####
#Assume tenants name is same as username
user='chasiumen'
passwd='admin'
mail='morinor@devtrax.com'
auth_url='http://controller:35357/v2.0'
cred='--os-username=' + user + ' --os-password=' + passwd + ' --os-tenant-name=' + tenant + ' --os-auth-url=' + auth_url


#### Keystone ####
#   1. Create user TENANT
#   2. Create user ACCOUNT
#   3. Assign user ROLE

#Create an instance
keystone = Keystone(user, passwd, mail)

#Create tenant
keystone.add_tenant()
#Create user
keystone.add_user()
#Assign role
keystone.add_role()



#execute a command
#a.exe('ls -al ./')
#a.router(user)
#b.add_tenant(user)



#output
#print dir(a)
#print a.output
