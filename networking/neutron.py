#!/usr/bin/python
import subprocess
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

######### NETWORK MANAGEMENT ########
#Class Neutron
class Net:
    def __init__(self, name, passwd):
        self.__name__ = name                            #name of instance
        self.user = name                                #User name
        self.passwd = passwd                            #User password
        #self.tenant = name                             #Tenant name
        self.tenant = 'testuser' #only on testrun
        self.auth_url='http://controller:35357/v2.0'    #authenticate URL
        #User Credential
        #neutron --os-username=chasiumen --os-password=agumion$0822 --os-tenant-name=testuser --os-auth-url=http://controller:35357/v2.0 subnet-list
        self.cred = '--os-username=' + self.user + ' --os-password=' + self.passwd + ' --os-tenant-name=' + self.tenant + ' --os-auth-url=' + self.auth_url
        self.name_priv='private-net'                    #Name of private netowrk
        self.name_subnet='private_subnet01'             #Name of subnet on private network
        self.NeuCmd = 'neutron ' + self.cred            #Neutron Base commad
        self.v= Verbose()
        self.v.notice('Created ' + colors.BLUE + name + colors.ENDC + ' [Net] instance successfully')
    
    #CREATE ROUTERS
    #neutron router-create [router_name]  + self.cred
    #neutron router-gateway-set [router_name] ext-net + self.cred
    #
    def router(self, router):
        self.router = router            #Name of router
        #Create new router
        cmd1=self.NeuCmd + ' router-create ' + self.router
        self.v.check(cmd1)
        self.v.notice('Created [' + self.router + '] router successfully')

        #Assign Gateway as ext-net
        cmd2=self.NeuCmd + ' router-gateway-set ' + self.router + ' ext-net '

        self.v.check(cmd2)
        self.v.notice('Assigned ext-net as [' + self.router + ']\'s gateway successfully')
        #self.exe(cmd1)
        #self.exe(cmd2)
       
    #CREATE INTERNAL NETWORKj
    #neutron net-create private-net --tenant-id $(source /root/admin-openrc.sh && keystone tenant-list | grep ' + self.tenant + ' | awk -F \'|\' \'{print $2}\')
    def add_network(self):
        tenant_id=' $(source /root/admin-openrc.sh && keystone tenant-list | grep ' + self.tenant + ' | awk -F \'|\' \'{print $2}\')'
        #Create network
        cmd1=self.NeuCmd + ' net-create ' + self.name_priv + tenant_id
        #Create subnet
        #neutron subnet-create private-net 10.0.0.0/24 --name private_subnet01 --enable_dhcp=True --gateway=10.0.0.1 --dns-nameserver 8.8.8.8
        cmd2=self.NeuCmd + ' subnet-create ' + self.name_priv + ' 10.0.0.0/24 --name ' + self.name_subnet + ' --enable_dhcp=True --gateway=10.0.0.1 --dns-nameserver 8.8.8.8'
        self.v.check(cmd1)
        self.v.check(cmd2)
        #self.exe(tenant_id)



        
    
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


#def get_tenant:
    #load admin cred
    #source /root/admin-openrc.sh
    ##export OS_USERNAME=admin
    ##export OS_PASSWORD=548295a7ebf749b74d42
    ##export OS_TENANT_NAME=admin
    ##export OS_AUTH_URL=http://controller:35357/v2.0
    #Get tenant list
