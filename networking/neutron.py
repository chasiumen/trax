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
    def __init__(self, name, passwd, KeyCmd):
        self.__name__ = name                            #name of instance
        self.user = name                                #User name
        self.passwd = passwd                            #User password
        self.tenant = name                             #Tenant name
        #self.tenant = 'testuser' #only on testrun
        self.auth_url='http://controller:35357/v2.0'    #authenticate URL
        #User Credential
        self.cred = '--os-username=' + self.user + ' --os-password=' + self.passwd + ' --os-tenant-name=' + self.tenant + ' --os-auth-url=' + self.auth_url
        self.name_priv='private-net'                    #Name of private netowrk
        self.name_subnet='private_subnet01'             #Name of subnet on private network
        self.NeuCmd = 'neutron ' + self.cred            #Neutron Base command
        self.KeyCmd = KeyCmd                            #keystone Base command
        self.v= Verbose()                               #Create Verbose instance
        self.v.notice('Created ' + colors.BLUE + name + colors.ENDC + '\'s [Net] instance successfully')
    
    #CREATE ROUTERS
    def router(self, router):
        self.router = router            #Name of router

        #Create new router              [neutron router-create ROUTER_NAME]
        cmd1=self.NeuCmd + ' router-create ' + self.router
        self.v.check(cmd1)
        self.exe(cmd1)
        self.v.notice('Created [' + self.router + '] router successfully')

        #Assign Gateway as ext-net      [neutron router-gateway-set ROUTER_NAME  ext-net]
        cmd2=self.NeuCmd + ' router-gateway-set ' + self.router + ' ext-net '
        self.v.check(cmd2)
        self.exe(cmd2)
        self.v.notice('Assigned ext-net as [' + self.router + ']\'s gateway successfully')
        
        #self.exe(cmd1)
        #self.exe(cmd2)
       
    #CREATE INTERNAL NETWORK
    #neutron net-create private-net --tenant-id $(source /root/admin-openrc.sh && keystone tenant-list | grep ' + self.tenant + ' | awk -F \'|\' \'{print $2}\')
    def add_network(self):
        #Get tenant_id and router_id
        self.tenant_id='$(' + self.KeyCmd + ' tenant-list | grep ' + self.tenant + ' | awk -F \'|\' \'{print $2}\')'
        self.router_id='$(' + self.NeuCmd + ' router-list | grep ' + self.router + ' | awk -F \'|\' \'{print $2}\')'
        
        #Create network                 [neutron net-create PRIVATE_NET_NAME --tenant-id=@#$A%^]
        cmd1=self.NeuCmd + ' net-create ' + self.name_priv + ' --tenant-id ' + self.tenant_id
        self.v.check(cmd1)
        self.exe(cmd1)
        self.v.notice('Created Network [' + colors.WHITE + self.name_priv + colors.ENDC + '] successfully')
        
        #Create subnet                  [neutron subnet-create private-net 10.0.0.0/24 --name private_subnet01 --enable_dhcp=True --gateway=10.0.0.1 --dns-nameserver 8.8.8.8]
        cmd2=self.NeuCmd + ' subnet-create ' + self.name_priv + ' 10.0.0.0/24 --name ' + self.name_subnet + ' --enable_dhcp=True --gateway=10.0.0.1 --dns-nameserver 8.8.8.8'
        self.v.check(cmd2)
        self.exe(cmd2)
        self.v.notice('Created Subnet [' + colors.WHITE + self.name_subnet + colors.ENDC + '] successfully')
        #self.exe(tenant_id)
        
        #Admin only 
        #update network as shared       [neutron net-update private-net --shared]
        cmd3=self.NeuCmd + ' net-update ' + self.name_priv + ' --shared'
        self.exe(cmd3)
        self.v.check(cmd3)
        
        #add interface                  [neutron router-interface-add  $router-id(r1's) INTERFACE(subnet=SUBNET_NAME)]
        cmd4=self.NeuCmd + ' router-interface-add ' + self.router_id + ' subnet=' +  self.name_subnet  #connect private network with router2
        self.v.check(cmd4)
        self.exe(cmd4)
        self.v.notice('Added interface [' + self.name_subnet + '] on router [' + self.router + '] successfully')

    ######## DELETE NETWORK AND ROUTER ###########
    def delete_network(self):
        #delete interface   router_id Interface
        cmd1=self.NeuCmd + ' router-interface-delete ' + self.router_id + ' subnet=' + self.name_subnet
        self.v.check(cmd1)
        self.exe(cmd2)
        self.v.warn('DELETE: router-interface [' + self.router + ']')
        
        #delete subnet
        cmd2 = self.NeuCmd + ' subnet-delete ' + self.name_subnet    
        self.v.check(cmd2)
        self.exe(cmd2)
        self.v.warn('DELETE: subent [' + self.name_subnet + ']')

        #delete network
        cmd3=self.NeuCmd + ' net-delete ' + self.name_priv
        self.v.check(cmd3)
        self.exe(cmd3)
        self.v.warn('DELETE: Private Network [' + self.name_priv + ']')

    def delete_router(self):
        #delete router
        cmd=self.NeuCmd + ' router-delete ' + self.router
        self.v.check(cmd)
        self.exe(cmd)
        self.v.warn('DELETE: router [' + self.router + ']')

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

