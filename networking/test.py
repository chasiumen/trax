#!/usr/bin/python

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


    if len(sys.argv) != 5:
        sys.exit("Need 4 argeuments")
    else:
        print "Argeument list:", str(sys.argv)

