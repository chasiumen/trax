#!/bin/bash -v
#Configure IP
sed -i s/ONBOOT=no/ONBOOT=yes/ /etc/sysconfig/network-scripts/ifcfg-eth0
service network restart

#Add repo
rpm -ivh http://yum.puppetlabs.com/el/6.4/products/x86_64/puppetlabs-release-6-7.noarch.rpm

#Install puppet client
yum install -y puppet

#Configure puppet client
sed -i s/#PUPPET_SERVER=puppet/PUPPET_SERVER=$ip_address/ /etc/sysconfig/puppet
sed -i s/#PUPPET_LOG=\/var\/log\/puppet\/puppet.log/PUPPET_LOG=\/var\/log\/puppet\/puppet.log/ /etc/sysconfig/puppet

#start puppet
service puppet start

#Have puppet run at startup
chkconfig puppet on

