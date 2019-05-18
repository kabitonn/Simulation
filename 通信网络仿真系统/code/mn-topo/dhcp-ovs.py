#!/usr/bin/env python
import os
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.link import Intf
from mininet.log import setLogLevel, info

def ToRealnet():

    #net = Mininet( topo=None, build=False)
    net = Mininet(controller=RemoteController)
    
	
    info( '*** Adding controller\n' )
    c0 = net.addController('c0',ip='127.0.0.1', port=6633)

    info( '*** Add switches\n')
    s1 = net.addSwitch('s1')
    
    info( '*** Add hosts\n')
    h1 = net.addHost('h1', ip='0.0.0.0',mac="00:00:00:00:00:01")
    h2 = net.addHost('h2', ip='0.0.0.0',mac="00:00:00:00:00:02")

    info( '*** Add links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    
    info( '*** Starting network\n')
    net.start()
    os.popen('ovs-vsctl add-port s1 eth1')       	## s1 host eth1
    os.system('sudo ifconfig eth1 0')
    h1.cmdPrint('dhclient '+h1.defaultIntf().name)      ## h1 DHCP IP
    h2.cmdPrint('dhclient '+h2.defaultIntf().name)      ## h2 DHCP IP
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    ToRealnet()
