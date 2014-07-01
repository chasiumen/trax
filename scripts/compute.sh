#!/bin/bash -x
#
#Service Password: 548295a7ebf749b74d42
#
#variables
#Controller node
CONT_MNG='10.0.0.11'
CONT_TUN='10.0.1.11'

#Network node
NET_MNG='10.0.0.21'
NET_TUN='10.0.1.21'

#Computer node
COMP_MNG='10.0.0.31'
COMP_TUN='10.0.1.31'

#Notes:
#	Network Config:
#		Managment Network:
#			Controller: 10.0.0.11
#			Network:	10.0.0.21
#			Compute 01:	10.0.0.31
#			Compute 02: 10.0.0.41
#			Compute 03: 10.0.0.51
#		Floating IPs:
#			NOT YET SET!
#		Tunnel Network:
#			Network:	10.0.1.21
#			Compute 01:	10.0.1.31
#			Compute 02: 10.0.1.41
#			Compute 03: 10.0.1.51
#		External Access:
#			Controller: 69.43.73.229
#			Network:	69.43.73.226
#			Compute 01:	69.43.73.227
#			Compute 02: 69.43.73.228
#			Compute 03: 69.43.73.???
#
#	Initial Setup:
#		yum install --enablerepo=epel ntp MySQL-python yum-plugin-priorities http://repos.fedorapeople.org/repos/openstack/openstack-icehouse/rdo-release-icehouse-3.noarch.rpm http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm openstack-utils openstack-selinux qpid-cpp-server -y;
#		yum upgrade -y;
#		reboot
#		service ntpd start;
#		chkconfig ntpd on;
#		service qpidd start;
#		chkconfig qpidd on;
#
#	Kernel functions:
#		/etc/sysctl.conf
#			net.ipv4.ip_forward=1
#			net.ipv4.conf.all.rp_filter=0
#			net.ipv4.conf.default.rp_filter=0
# 		sysctl -p
#	Hosts:
#		add 'controller' to host with the management IP




### Nova Setup ###
echo "Installing Compute Service (Nova)...";
yum install --enablerepo=epel openstack-nova-compute -y;
echo "Done.";

echo "Configuring Nova...";
openstack-config --set /etc/nova/nova.conf database connection mysql://nova:548295a7ebf749b74d42@controller/nova;
openstack-config --set /etc/nova/nova.conf DEFAULT auth_strategy keystone;
openstack-config --set /etc/nova/nova.conf keystone_authtoken auth_uri http://controller:5000;
openstack-config --set /etc/nova/nova.conf keystone_authtoken auth_host controller;
openstack-config --set /etc/nova/nova.conf keystone_authtoken auth_protocol http;
openstack-config --set /etc/nova/nova.conf keystone_authtoken auth_port 35357;
openstack-config --set /etc/nova/nova.conf keystone_authtoken admin_user nova;
openstack-config --set /etc/nova/nova.conf keystone_authtoken admin_tenant_name service;
openstack-config --set /etc/nova/nova.conf keystone_authtoken admin_password 548295a7ebf749b74d42;
openstack-config --set /etc/nova/nova.conf DEFAULT rpc_backend qpid
openstack-config --set /etc/nova/nova.conf DEFAULT qpid_hostname controller;
openstack-config --set /etc/nova/nova.conf DEFAULT my_ip $COMP_MNG;
openstack-config --set /etc/nova/nova.conf DEFAULT vnc_enabled True;
openstack-config --set /etc/nova/nova.conf DEFAULT vncserver_listen 0.0.0.0;
openstack-config --set /etc/nova/nova.conf DEFAULT vncserver_proxyclient_address $COMP_MNG;
openstack-config --set /etc/nova/nova.conf DEFAULT novncproxy_base_url http://controller:6080/vnc_auto.html;
openstack-config --set /etc/nova/nova.conf DEFAULT glance_host controller;
# Check this before running
# openstack-config --set /etc/nova/nova.conf libvirt virt_type qemu;
echo "Done.";

echo "Starting service and setting chkconfig...";
service libvirtd start;
service messagebus start;
chkconfig libvirtd on;
chkconfig messagebus on;
service openstack-nova-compute start;
chkconfig openstack-nova-compute on;
echo "Done.";

echo "Installing Networking Service (Neutron)...";
yum install openstack-neutron-ml2 openstack-neutron-openvswitch -y;
echo "Done.";

echo "Configuring Neutron...";
openstack-config --set /etc/neutron/neutron.conf DEFAULT auth_strategy keystone;
openstack-config --set /etc/neutron/neutron.conf keystone_authtoken auth_uri http://controller:5000;
openstack-config --set /etc/neutron/neutron.conf keystone_authtoken auth_host controller;
openstack-config --set /etc/neutron/neutron.conf keystone_authtoken auth_protocol http;
openstack-config --set /etc/neutron/neutron.conf keystone_authtoken auth_port 35357;
openstack-config --set /etc/neutron/neutron.conf keystone_authtoken admin_tenant_name service;
openstack-config --set /etc/neutron/neutron.conf keystone_authtoken admin_user neutron;
openstack-config --set /etc/neutron/neutron.conf keystone_authtoken admin_password 548295a7ebf749b74d42;
openstack-config --set /etc/neutron/neutron.conf DEFAULT rpc_backend neutron.openstack.common.rpc.impl_qpid;
openstack-config --set /etc/neutron/neutron.conf DEFAULT qpid_hostname controller;
openstack-config --set /etc/neutron/neutron.conf DEFAULT core_plugin ml2;
openstack-config --set /etc/neutron/neutron.conf DEFAULT service_plugins router;
openstack-config --set /etc/neutron/plugins/ml2/ml2_conf.ini ml2 type_drivers gre;
openstack-config --set /etc/neutron/plugins/ml2/ml2_conf.ini ml2 tenant_network_types gre;
openstack-config --set /etc/neutron/plugins/ml2/ml2_conf.ini ml2 mechanism_drivers openvswitch;
openstack-config --set /etc/neutron/plugins/ml2/ml2_conf.ini ml2_type_gre tunnel_id_ranges 1:1000;
openstack-config --set /etc/neutron/plugins/ml2/ml2_conf.ini ovs local_ip $COMP_TUN;
openstack-config --set /etc/neutron/plugins/ml2/ml2_conf.ini ovs tunnel_type gre;
openstack-config --set /etc/neutron/plugins/ml2/ml2_conf.ini ovs enable_tunneling True;
openstack-config --set /etc/neutron/plugins/ml2/ml2_conf.ini securitygroup firewall_driver neutron.agent.linux.iptables_firewall.OVSHybridIptablesFirewallDriver;
openstack-config --set /etc/neutron/plugins/ml2/ml2_conf.ini securitygroup enable_security_group True;
echo "Done.";

echo "Enabling OVS...";
service openvswitch start;
chkconfig openvswitch on;
ovs-vsctl add-br br-int;
echo "Done.";

echo "Configuring Nova...";
openstack-config --set /etc/nova/nova.conf DEFAULT network_api_class nova.network.neutronv2.api.API;
openstack-config --set /etc/nova/nova.conf DEFAULT neutron_url http://controller:9696;
openstack-config --set /etc/nova/nova.conf DEFAULT neutron_auth_strategy keystone;
openstack-config --set /etc/nova/nova.conf DEFAULT neutron_admin_tenant_name service;
openstack-config --set /etc/nova/nova.conf DEFAULT neutron_admin_username neutron;
openstack-config --set /etc/nova/nova.conf DEFAULT neutron_admin_password 548295a7ebf749b74d42;
openstack-config --set /etc/nova/nova.conf DEFAULT neutron_admin_auth_url http://controller:35357/v2.0;
openstack-config --set /etc/nova/nova.conf DEFAULT linuxnet_interface_driver nova.network.linux_net.LinuxOVSInterfaceDriver;
openstack-config --set /etc/nova/nova.conf DEFAULT firewall_driver nova.virt.firewall.NoopFirewallDriver;
openstack-config --set /etc/nova/nova.conf DEFAULT security_group_api neutron;
echo "Done.";

echo "Completing settup..."
ln -s /etc/neutron/plugins/ml2/ml2_conf.ini /etc/neutron/plugin.ini;
cp /etc/init.d/neutron-openvswitch-agent /etc/init.d/neutron-openvswitch-agent.orig;
sed -i 's,plugins/openvswitch/ovs_neutron_plugin.ini,plugin.ini,g' /etc/init.d/neutron-openvswitch-agent;
service openstack-nova-compute restart;
service neutron-openvswitch-agent start;
chkconfig neutron-openvswitch-agent on;
### Configur networks later ###

### Cinder Setup ###
echo "Installing Block Storage Service (Cinder)...";
yum install openstack-cinder scsi-target-utils -y;
echo "Done.";

echo "Configuring Cinder...";
openstack-config --set /etc/cinder/cinder.conf DEFAULT auth_strategy keystone;
openstack-config --set /etc/cinder/cinder.conf keystone_authtoken auth_uri http://controller:5000;
openstack-config --set /etc/cinder/cinder.conf keystone_authtoken auth_host controller;
openstack-config --set /etc/cinder/cinder.conf keystone_authtoken auth_protocol http;
openstack-config --set /etc/cinder/cinder.conf keystone_authtoken auth_port 35357;
openstack-config --set /etc/cinder/cinder.conf keystone_authtoken admin_user cinder;
openstack-config --set /etc/cinder/cinder.conf keystone_authtoken admin_tenant_name service;
openstack-config --set /etc/cinder/cinder.conf keystone_authtoken admin_password 548295a7ebf749b74d42;
openstack-config --set /etc/cinder/cinder.conf DEFAULT rpc_backend cinder.openstack.common.rpc.impl_qpid;
openstack-config --set /etc/cinder/cinder.conf DEFAULT qpid_hostname controller;
openstack-config --set /etc/cinder/cinder.conf database connection mysql://cinder:548295a7ebf749b74d42@controller/cinder;
openstack-config --set /etc/cinder/cinder.conf DEFAULT glance_host controller;
echo "Done.";

echo "Starting services...";
service openstack-cinder-volume start;
service tgtd start;
chkconfig openstack-cinder-volume on;
chkconfig tgtd on;
echo "Done.";
