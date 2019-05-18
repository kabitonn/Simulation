#!/usr/bin/python
# -*- coding: utf-8 -*-

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.log import setLogLevel,info,error
from mininet.topo import Topo
from mininet.node import RemoteController
from mininet.node import Controller
import os


Host_Num=4
Switch_Num=3

class MyTopo(Topo):
	def __init__(self):
		Topo.__init__(self)

		switches = [ self.addSwitch('s' + str(i+1)) for i in range(Switch_Num) ]
		hosts    = [ self.addHost('h' + str(i+1)) for i in range(Host_Num) ]
	
		for i in range(len(hosts)):
			self.addLink(hosts[i],switches[i/(Host_Num/(Switch_Num-1))+1])
		for i in range(len(switches)-1):
			self.addLink(switches[i+1],switches[0])



def configNet():
	
	mytopo=MyTopo()
	net = Mininet( topo=mytopo,controller=None) 
	switch=net.switches[ 0 ] 
	
	c0 = RemoteController( 'c0', ip='127.0.0.1', port=6653 )
	net.addController(c0)
	net.start()
	hosts=mytopo.hosts()
	print hosts
	[net.get(hosts[i]).setMAC('10:00:00:00:00:'+str(i+1))for i in range(len(hosts))]
	[net.get(hosts[i]).setIP('192.0.0.'+str(i+1),21)for i in range(len(hosts))]
	[net.get(hosts[i]).cmd('route add -net 192.0.0.0/4 dev ' + hosts[i] + '-eth0')for i in range(len(hosts))]
	
	# os.system('sudo ovs-vsctl add-port %s eth1' % switch)
	#os.system('sudo ifconfig eth1 0')
	#os.system('sudo ifconfig s1 10.33.11.254')
	#net.get(switch).cmd('ifconfig eth1 0')
	#net.get(switch).cmd('route add -net 10.33.8.0/22 dev eth1')
	#net.get(switch).cmd('route add -net 10.0.0.0/21 gw 10.0.0.254')
	

	CLI( net )
	net.stop()



if __name__ == '__main__':
	setLogLevel( 'info' )
	configNet()
	
'''
	os.system('sudo ovs-vsctl add-port s1 eth1')
    os.system('sudo ifconfig eth1 0')
    os.system('sudo ifconfig s1 10.33.11.254/25')
'''
		
		

	    

