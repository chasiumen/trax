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


######### Account Management #########
#Class Keystone
#--os-username=admin --os-password=548295a7ebf749b74d42 --os-tenant-name=admin --os-auth-url=http://controller:35357/v2.0
class Keystone:
    def __init__(self, name, passwd):
    #Regular user
        self.name = name                                #Name of instance
        self.passwd = passwd                            #User password
        self.tenant = name                             #Name of user Tenant
        self.desc = 'User Tenant'
        #self.role = 'admin'                             #Role of the user
        self.role = '_member_'                          #Role of the user (default regular user)
    #Admin Cred //Static
        self.admin_pass = '548295a7ebf749b74d42'        #Admin's pass
        self.admin_tenant = 'admin'                     #Admin's tenant (admin)
        self.auth_url = 'http://controller:35357/v2.0'  #Auth URL
        self.admin_cred = '--os-username=admin  --os-password=' + self.admin_pass + ' --os-tenant-name=' + self.admin_tenant + ' --os-auth-url=' + self.auth_url
        self.KeyCmd ='keystone ' + self.admin_cred
    #Output
        self.v= Verbose()                           #Create Verbose instance
        self.v.notice('Created ' + colors.BLUE + name + colors.ENDC + '\'s ' + '[Keyston] instance successfully')
    
    #           -------------------- CREATE FUNCTIONS --------------------
    #
    #CREATE TENANTS
    #keystone tenant-create --name=testuser --description="Test User Tenant"
    #
    def add_tenant(self):
        cmd =self.KeyCmd + ' tenant-create --name=' + self.tenant + ' --description=\"' + self.desc + '\"'
        self.v.check(cmd)
        self.v.notice('Creating  User account')
        self.exe(cmd)
        
    #CREATE USERS 
    #keystone user-create --name=chasiumen --pass=admin --email=morinor@devtrax.com
    #    
    def add_user(self, mail):
        self.email = email                              #User email
        cmd =self.KeyCmd +  ' user-create --name=' + self.name + ' --pass=' + self.passwd + ' --email=' + self.email
        self.v.check(cmd)
        self.v.notice('Creating User tenant')
        self.exe(cmd)

    #ADD ROLE 
    #keystone user-role-add --user=chasiumen --role=admin/member --tenant=testuser
    #    
    def add_role(self):
        cmd =self.KeyCmd + ' user-role-add --user=' + self.name + ' --role=' + self.role + ' --tenant=' + self.tenant
        self.v.check(cmd)
        self.v.notice('Adding ' + self.name + ' as [' + self.role + ']')
        self.exe(cmd)

    #
    #           -------------------- REMOVE FUNCTIONS --------------------
    #DELETE TENANTS
    #keystone user-role-remove --user=chasiumen --role=_member_ --tenant=testuser
    #
    def del_tenant(self):
        cmd =self.KeyCmd + ' tenant-delete ' + self.tenant
        self.v.check(cmd)
        self.v.warn('DELETE: User tenant [' +  self.tenant + ']')
        self.exe(cmd)

    #DELETE TENANTS
    #keystone tenant-delete testuser
    #
    def del_user(self):
        cmd =self.KeyCmd + ' user-delete ' + self.name
        self.v.check(cmd)
        self.v.warn('DELETE: User [' + self.name + ']')
        self.exe(cmd)

    def get_user(self):
        cmd =self.KeyCmd + ' user-list'
        self.exe(cmd)
        self.v.check(cmd)

    #execute shell comannd
    def exe(self, cmd):
        p =subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate()
        self.output = out.rstrip()
        return self.output


#Verbose class -simple colored outputs-
class Verbose(object):
    #Default output
    def __init__(self):
        print 'Color instance created'
    def notice(self, cmd):
        print colors.GREEN + cmd + colors.ENDC   
    #Warning message
    def warn(self, cmd):
        print colors.RED + cmd + colors.ENDC
    #Command check
    def check(self, cmd):
        print 'CMD:' + colors.WHITE + cmd + colors.ENDC


