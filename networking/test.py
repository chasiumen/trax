#!/usr/bin/python

import sys, os.path, subprocess

##load additonal modules
#mPath='./lib/'
#if os.path.isfile(mPath+'neutron.py') and os.path.isfile(mPath+'keystone.py') is False:
#    sys.exit("Error: Unable to load modules")
#else:
#    sys.path.append(mPath)
#    import neutron
#    print "Module [neutron] added..."
#    import keystone
#    print "Module [keyston] added..."
#
#
#    if len(sys.argv) != 5:
#        sys.exit("Need 4 argeuments")
#    else:
#        print "Argeument list:", str(sys.argv)
#
#
#
#execute shell comannd
def exe(cmd):
    p =subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    output = out.rstrip()
    print "OUTPUT:"+ output
    print "ERROR:" + str(err)
    return output


exe('cat /etc/fstab')

