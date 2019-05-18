#!/usr/bin/python
import time
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch,UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink

def topology():

    "Create a network."
    net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch )

    print "*** Creating nodes ***"
    h1 = net.addHost( 'h1', mac='00:00:00:00:00:01', ip='10.0.10.1/24' )
    h2 = net.addHost( 'h2', mac='00:00:00:00:00:02', ip='10.0.10.2/24' )
    h3 = net.addHost( 'h3', mac='00:00:00:00:00:03', ip='10.0.1.1/24' )
    s1 = net.addSwitch( 's1', listenPort=6673, mac='00:00:00:00:00:11' )
    s2 = net.addSwitch( 's2', listenPort=6674, mac='00:00:00:00:00:12' )
    c0 = net.addController( 'c0', controller=RemoteController, ip='127.0.0.1', port=6633 )

    print "*** Creating links ***"
    net.addLink(s1, h1, 1, 0)
    net.addLink(s2, h3, 1, 0)

    Link(h2, s1, intfName1='h2-eth0')
    Link(h2, s2, intfName1='h2-eth1')
    h2.cmd('ifconfig h2-eth1 10.0.1.2 netmask 255.255.255.0')
    h2.cmd('sysctl net.ipv4.ip_forward=1')

   

    print "*** Starting network ***"
    net.build()
    c0.start()
    s1.start( [c0] )
    s2.start( [c0] )
    h1.cmd('route add default gw 10.0.10.2')
    h3.cmd('route add default gw 10.0.1.2')
    print "*** Running CLI ***"
    CLI( net )

    print "*** Stopping network ***"
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()

