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
class Keystone:
    def __init__(self, name, passwd, email):
        self.name = name
        self.passwd = passwd
        self.email = email
        self.tenant = name
        self.desc = 'User Tenant'
        self.role = 'admin'
        self.admin_pass = '548295a7ebf749b74d42'
        self.admin_tenant = 'admin'
        self.auth_url = 'http://controller:35357/v2.0'
        #--os-username=admin --os-password=548295a7ebf749b74d42 --os-tenant-name=admin --os-auth-url=http://controller:35357/v2.0
        self.admin_cred = '--os-username=admin  --os-password=' + self.admin_pass + ' --os-tenant-name=' + self.admin_tenant + ' --os-auth-url=' + self.auth_url
        print 'Created ' + colors.WHITE + name + colors.ENDC + '\'s ' + '[Keyston] instance successfully'
    
    #           -------------------- CREATE FUNCTIONS --------------------
    #
    #CREATE TENANTS
    #keystone tenant-create --name=testuser --description="Test User Tenant"
    #
    def add_tenant(self):
        cmd ='keystone tenant-create --name=' + self.tenant + ' --description=\"' + self.desc + '\"'
        print 'CMD:'+ colors.WHITE + cmd + colors.ENDC
        print colors.GREEN + 'Created User account successfully' + colors.ENDC

    #CREATE USERS 
    #keystone user-create --name=chasiumen --pass=admin --email=morinor@devtrax.com
    #    
    def add_user(self):
        cmd = 'keystone user-create --name=' + self.name + ' --pass=' + self.passwd + ' --email=' + self.email
        print 'CMD:'+ colors.WHITE + cmd + colors.ENDC
        print colors.GREEN + 'Created User tenant successfully' + colors.ENDC

    #ADD ROLE 
    #keystone user-role-add --user=chasiumen --role=admin/member --tenant=testuser
    #    
    def add_role(self):
        cmd = 'keystone user-role-add --user=' + self.name + ' --role=' + self.role + ' --tenant=' + self.tenant
        print 'CMD:'+ colors.WHITE + cmd + colors.ENDC
        print colors.GREEN + 'Add ' + self.name + ' as [' + self.role + '] successfully' + colors.ENDC

    #
    #           -------------------- REMOVE FUNCTIONS --------------------
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

    #execute shell comannd
    def exe(self, cmd):
        p =subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate()
        self.output = out.rstrip()
        return self.output

