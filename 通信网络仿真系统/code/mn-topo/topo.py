#!/usr/bin/python
# -*- coding: utf-8 -*-

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.log import setLogLevel,info,error
from mininet.topo import Topo
from mininet.node import RemoteController
from mininet.node import Controller

import json
import os



class MyTopo(Topo):
    def __init__(self, filepath):
        Topo.__init__(self)

        self.Nodes = []
        self.Switches = {}
        self.Hosts = {}
        self.Links = []
        self.process_json(filepath)
        self.create_node_link()



    def create_node_link(self):
        switches = [ self.addSwitch(sw, **self.Switches[sw]) for sw in self.Switches ]
        hosts    = [ self.addHost(h, **self.Hosts[h] )for h in self.Hosts ]
        for link in self.Links:
            self.addLink(link['src'], link['dst'])
        # print self.g.node 

    def process_json(self, filepath):
        f = open(filepath, 'r')
        topo_dict = json.load(f)
        section = topo_dict['section']
        nodes = topo_dict['nodes']
        edges = topo_dict['edges']
        for node in nodes:
            name = str(node['name'])
            node_type = str(node['type'])
            attr = {}
            attr['type'] = node_type
            attr['location'] = [float(x) for x in node['location']]
            if node_type == 'host' or node_type == 'server':
                attr['ip'] = str(node['ip'])
                attr['mac'] = str(node['mac'])
                self.Hosts[name] = attr
                # print(self.Hosts[name]['mac'])
            elif node_type == 'switch' or node_type == 'router':
                self.Switches[name] = attr
                # print(self.Switches[name])
            self.Nodes.append(name)

        for edge in edges:
            src = str(edge['source'])
            dst = str(edge['target'])
            link = {'src':src,'dst':dst}
            self.Links.append(link)
            # print(link)
        print("hosts num:%d\nswitches num:%d" %(len(self.Hosts),len(self.Switches)))
        print("links num:%d" %(len(self.Links)))


def configNet():
    mytopo = MyTopo("mininet/custom/topo.json")
    net = Mininet(topo=mytopo, controller=None)
    
    c0 = RemoteController( 'c0', ip='192.168.2.1', port=6653 )
    net.addController(c0)
    net.start()

    hosts = mytopo.hosts()
    for host in hosts:
        net.get(host).setMAC(mytopo.Hosts[host]['mac'])
        net.get(host).setIP(mytopo.Hosts[host]['ip'])
        net.get(host).cmd('route add -net default dev ' + host + '-eth0')
   
    CLI( net )
    net.stop()



if __name__ == "__main__":
    setLogLevel( 'info' )
    configNet()
    
