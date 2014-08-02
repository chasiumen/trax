#!/bin/bash -v
#Configure IP
#sed -i s/ONBOOT=no/ONBOOT=yes/ /etc/sysconfig/network-scripts/ifcfg-eth0
#sed -i s/BOOTPROTO=dhcp/ONBOOT=none/ /etc/sysconfig/network-scripts/ifcfg-eth0
#echo IPADDR=$ip_address >> /etc/sysconfig/network-scripts/ifcfg-eth0
#echo NETMASK=$netmask >> /etc/sysconfig/network-scripts/ifcfg-eth0
#echo GATEWAY=$gateway >> /etc/sysconfig/network-scripts/ifcfg-eth0
#service network restart

#Add repo
#rpm -ivh http://yum.puppetlabs.com/el/6.4/products/x86_64/puppetlabs-release-6-7.noarch.rpm

#Install Puppet Master
#yum install -y puppet-server
apt-get install puppetmaster
#Configure puppet Master
echo \* > /etc/puppet/autosign.conf


#start Puppet-Server
#service puppetmaster start
/etc/init.d/puppetmaster restart
#Have Puppet Master run at startup
#chkconfig puppetmaster on

