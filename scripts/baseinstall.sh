#!/bin/bash
#Installs basic dependancies
#
# MySQL:
#	[mysqld]
#	...
#	default-storage-engine = innodb
#	innodb_file_per_table
#	collation-server = utf8_general_ci
#	init-connect = 'SET NAMES utf8'
#	character-set-server = utf8
#
#	mysql_secure_installation
#
# Qpid:
#	/etc/qpidd.conf
#		auth=no
yum install ntp mysql mysql-server MySQL-python yum-plugin-priorities http://repos.fedorapeople.org/repos/openstack/openstack-icehouse/rdo-release-icehouse-3.noarch.rpm http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm openstack-utils openstack-selinux qpid-cpp-server -y; yum upgrade -y;

#Service config
service ntpd start;chkconfig ntpd on;service mysqld start;chkconfig mysqld on;service qpidd start;chkconfig qpidd on;