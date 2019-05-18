#!/usr/bin/python
# -*- coding: utf-8 -*-

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.log import setLogLevel,info,error
from mininet.topo import Topo
from mininet.node import RemoteController
from mininet.node import Controller
import os

#import pudb
#pudb.set_trace()

Host_Num=8
Switch_Num=3

class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        switches = [ self.addSwitch('s' + str(i+1),location='100,100') for i in range(Switch_Num) ]
        hosts    = [ self.addHost('h' + str(i+1),location='100,100') for i in range(Host_Num) ]
                
        print self.g.node  
        for i in range(len(hosts)):
            self.addLink(hosts[i],switches[i/(Host_Num/(Switch_Num-1))+1])
        for i in range(len(switches)-1):
            self.addLink(switches[i+1],switches[0])



def configNet():
    
    mytopo=MyTopo()
    net = Mininet( topo=mytopo,controller=None) 
    switch=net.switches[ 0 ] 
    
    c0 = RemoteController( 'c0', ip='127.0.0.1', port=6633 )
    net.addController(c0)
    net.start()
    hosts=mytopo.hosts()
    #os.system('sudo ovs-vsctl add-port %s eth1' %switch)

    [net.get(hosts[i]).setMAC('10:00:00:00:00:'+str(i+1))for i in range(len(hosts))]
    [net.get(hosts[i]).setIP('10.33.8.'+str(i+1),24)for i in range(len(hosts)/2)]
    [net.get(hosts[i]).setIP('10.0.0.'+str(i+1),24) for i in range(len(hosts)/2,len(hosts))]
    #[net.get(hosts[i]).cmdPrint('dhclient '+ net.get(hosts[i]).defaultIntf().name)for i in range(len(hosts))]
    [net.get(hosts[i]).cmd('route add default dev ' + hosts[i] + '-eth0')for i in range(len(hosts))]
    #[net.get(hosts[i]).cmd('route add -net 10.0.0/8 dev ' + hosts[i] + '-eth0')for i in range(len(hosts))]
    
    
    #os.system(' ifconfig eth1 0 up && ifconfig s1 10.33.8.233/24 up')
    #os.system(' route add default gw 10.33.8.2 s1')
    #os.system('sudo ifconfig s1 10.33.11.254')
    #net.get(switch).cmd('ifconfig eth1 0')
    #net.get(switch).cmd('route add -net 10.33.8.0/22 dev eth1')
    #net.get(switch).cmd('route add -net 10.0.0.0/21 gw 10.0.0.254')
    
    print(net.nameToNode['h1'].params)

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
        
        

        

