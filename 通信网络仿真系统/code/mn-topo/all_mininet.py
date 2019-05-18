#!/usr/bin/python
# -*- coding: utf-8 -*-

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.topo import Topo
from mininet.node import RemoteController
from mininet.node import Controller
import os


def addFlows(hide, priority=0):
    for i in range(1, 9):
        if i not in hide:
            os.system("ovs-ofctl add-flow s%d priority=%d,actions=CONTROLLER:65535" % (i, priority))

def topoDiscover():
    topo = MyTopo()

    #net = Mininet(topo=topo, link=TCLink, controller=RemoteController)
    net = Mininet( topo=topo,controller=lambda name: RemoteController( name,ip='127.0.0.1',port=6633))
    #net = Mininet(topo=topo, link=TCLink)
    # 启动Mininet
    net.start()

    hosts = topo.hosts()
    try:
        # 配置Hosts的MAC地址
        [ net.get(hosts[i]).setMAC('10:00:00:00:00:'+str(i+1)) for i in range(len(hosts)) ]
        [net.get(hosts[i]).setIP('10.0.0.'+str(i+3), 24) for i in range(len(hosts))]
        # 执行各种命令
        [ net.get(hosts[i]).cmd('route add -net 10.0.0.0/24 dev ' + hosts[i] + '-eth1') for i in range(len(hosts)) ]
        os.system('sudo ovs-vsctl add-port s1 eth1')
        os.system('sudo ifconfig eth1 0')
        os.system('sudo ifconfig s1 10.0.0.254/24')
	os.system('sudo route add default gw <nat_ip> s1 ')
	os.system('sudo route del default gw <nat_ip> eth1 ')

	CLI(net)
	net.stop()


    except Exception,e:
        print e
        net.stop()

class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        switches_num = 5
        hosts_num = 10

        switches = [ self.addSwitch('s' + str(i+1)) for i in range(switches_num) ]
        hosts    = [ self.addHost('h' + str(i+1)) for i in range(hosts_num) ]
        self.addLink(hosts[0], switches[0])
	self.addLink(hosts[1], switches[0])
	self.addLink(hosts[2], switches[1])
	self.addLink(hosts[3], switches[1])
	self.addLink(hosts[4], switches[2])
	self.addLink(hosts[5], switches[2])
	self.addLink(hosts[6], switches[3])
	self.addLink(hosts[7], switches[3])
	self.addLink(hosts[8], switches[4])
	self.addLink(hosts[9], switches[4])
	self.addLink(switches[0], switches[1])
	self.addLink(switches[1], switches[2])
	self.addLink(switches[2], switches[3])
	self.addLink(switches[3], switches[4])
	self.addLink(switches[4], switches[0])




if __name__ == '__main__':
    setLogLevel('info')
    topoDiscover()
