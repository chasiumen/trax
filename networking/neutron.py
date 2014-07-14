#!/usr/bin/python
import subprocess

#### VARIABLES ####
user='chasiumen'
passwd='admin'
#Assume tenants name is same as username
tenant=user
auth_url='http://controller:35357/v2.0'
cred='--os-username=' + user + ' --os-password=' + passwd + ' --os-tenant-name=' + tenant + ' --os-auth-url=' + auth_url







class Net:
    def __init__(self, name):
        self.__name__ = name
       # self.user = user
       # self.passwd = passwd
       # self.tenant = user
       # self.auth_url='http://controller:35357/v2.0'
       # self.cred = '--os-username=' + user + ' --os-password=' + passwd + ' --os-tenant-name=' + tenant + ' --os-auth-url=' + auth_url
        print 'Created [Net] instance successfully'
    
    #add a router
    def router(self, name):
        self.__name__ = name
        
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



#create an instance
a=Net(user)

#execute a command
#a.exe('ls -al ./')
a.router(user)



#output
print dir(a)
print a.output
