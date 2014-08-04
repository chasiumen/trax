#!/usr/bin/python
#nova.py

import sys, re, subprocess

########################## FUNCTIONS ###############################
#nova --os-username=umi --os-password=admin --os-tenant-name=umi --os-auth-url=http://controller:35357/v2.0 list
#Generates dynamic bash commands
def cmd(path, cred, x):
#    cmd = 'nova os-username=umi --os-password=admin --os-tenant-name=umi --os-auth-url=http://controller:35357/v2.0 list' +  ' |  awk -F \'\|\' \'{print $' + x + '}\' '
#    cmd = 'nova ' + cred + ' list  \|  awk -F \'\|\' \'{print $' + x + '}\' '
    cmd = 'cat ' + path +  ' |  awk -F \'|\' \'{print $' + x + '}\' '
#    print cmd
    return exe(cmd)

#execute shell comannd
def exe(cmd):
    p =subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    #self.output = out.rstrip()
    output = out.rstrip()
    return parse(output)
    
#Parsing
def parse(line):
    x = re.split(r"\s+",line)
#    print "parse", x
    return x


def php_out(NovaCmd, ID, NAME, STATUS, POWER, x, console):
    #print '<tr><td><h6>' + array[x] + '</h2></td><td><input type="submit" formaction="" value="Soft Reboot" /></td><td><input type="submit" formaction="" value="Delete" /></td><td><input type="submit" formaction="" value="Console" /></td></tr><br />'
    pipe = ' | '
#    print console + pipe +  NAME[x] + pipe + STATUS[x] + pipe + POWER[x] + '\n'
    print " <?php session_start(); $=\""+ ID + "; $_SESSION[\"ID\"]=$ID; ?> <form id=\"instances\" method=\"post\" action=\"\"> <table summary=\"instances\"> <tr> <td><h2>" + NAME[x] +  "</h2></td> <td><input type=\"submit\" formaction=\"reboot.php  \" value=\"Soft Reboot\" /></td> <td><input type=\"submit\" formaction=\"" "\" value=\"Delete\" /></td><td><input type=\"submit\" formaction=\"" + console  + "\" value=\"Console\" /></td> </tr> <br /> "
    print "</table> </form>"


#    print " <?php
#session_start();
#$=\""+ ID + ";
#$_SESSION[\"ID\"]=$ID;
#?>
#<form id=\"instances\" method=\"post\" action=\"\">
#<table summary=\"instances\">
#<tr>
#<td><h2>" + NAME[x] +  "</h2></td>
#<td><input type=\"submit\" formaction=\"reboot.php  \" value=\"Soft Reboot\" /></td>
#<td><input type=\"submit\" formaction=\"" "\" value=\"Delete\" /></td>
#<td><input type=\"submit\" formaction=\"" + console  + "\" value=\"Console\" /></td>
#</tr>
#<br />
#"
#    reboot(NovaCmd, ID)
#    terminate(NovaCmd, ID)

################ NOVA RELATED FUNCTIONS
#nova cred + get-vnc-console InstanceID novnc
def get_console(NovaCmd,InstanceID):
    cmd = NovaCmd + ' get-vnc-console ' +  InstanceID + ' novnc'
#    print "GetConsole:"
    x = exe(cmd)
#    print x[11]
    return x[11]
#SOFT REBOOT
def reboot(NovaCmd, InstanceID):
    cmd = NovaCmd + ' reboot ' + InstanceID
    #exe(cmd)
#    print "Reboot:" + cmd

#STOP
def terminate(NovaCmd, InstanceID):
    cmd= NovaCmd + ' stop ' + InstanceID
    #exe(cmd)
#    print "Terminate:" + cmd



##################### MAIN ###############
#dir of nova-list output
#path='../conf/instance.out'
path='/tmp/instance.out'

#check number of arguments
#User pass 
if len(sys.argv) != 3:
    print "Error: Number of command-line argument mismatch"
    sys.exit("Usage: ./nova USER PASSWD")
else:
    user=sys.argv[1]
    passwd=sys.argv[2]
    tenant=user
    auth_url = 'http://controller:35357/v2.0'  #Auth URL
    cred = '--os-username=' + user +  ' --os-password=' + passwd + ' --os-tenant-name=' + tenant + ' --os-auth-url=' + auth_url
    NovaCmd = 'nova ' + cred                   #nova base command
    
    #Get list of instances and output to a file
    GetList = NovaCmd + ' list > ' + path
    outfile = exe(GetList)

#INSTANCE ID
    #cat ../conf/instance.out  | awk -F '\|' '{print $3}'
    InstanceID = cmd(path, cred, '2')
    del InstanceID[0:2]         #trim data
    #print "InstnceID", InstanceID
    
#NAME OF INSTANCE
    InstanceName = cmd(path, cred, '3')
    del InstanceName[0:2]       #trim data
    #print "InstanceName:", InstanceName
    
#Instance Status
    #cat ../conf/instance.out  | awk -F '\|' '{print $4}'
    #active
    #shutoff
    InstanceStatus = cmd(path, cred, '4')
    del InstanceStatus[0:2]
    #print "Instance Status:", InstanceStatus
    
#power state
    #cat ../conf/instance.out  | awk -F '\|' '{print $6}'
    #Running 
    #shutdown
    PowerState = cmd(path, cred, '6')
    del PowerState[0:3]         #trim data
    #print "Power State:",  PowerState

    print '====='*10
    
    for x in range(0,len(InstanceName)):
        console = get_console(NovaCmd, InstanceID[x])
        php_out(NovaCmd, InstanceID, InstanceName, InstanceStatus, PowerState, x, console)
