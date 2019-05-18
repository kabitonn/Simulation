#!/usr/bin/python
# -*- coding: utf-8 -*-

from mininet.cli import CLI
from mininet.log import info, error
from mininet.term import cleanUpScreens, makeTerms
import os
import signal
import json
import time

import topo_create
import topo_get

class Net(object):
    def __init__(self):
        
        self.nodes = {}
        self.edges = {}
        self.lines = []
        self.hosts = []
        self.switches = []
        self.terms = []
        self.map2name = {}
        self.net = topo_create.net
        self.process_topo()
        # time.sleep(1)
        self.topo = topo_get.Topo()
        # self.topo.print_edges()

        


    def cmd_host(self, host_name, cmd):
        host = self.net.get(host_name)
        host.cmdPrint(cmd)

    def ping_host(self, h1, h2):
        host1 = self.net.get(h1)
        host2 = self.net.get(h2)
        output = host1.cmd('ping -c 1 %s' % host2.IP())
        return output

    def start_xterm(self, host_name):
        "Start a terminal for each node."
        if 'DISPLAY' not in os.environ:
            error( "Error starting terms: Cannot connect to display\n" )
            return
        info( "*** Running terms on %s\n" % os.environ[ 'DISPLAY' ] )
        cleanUpScreens()
        self.terms += makeTerms([self.net.get(host_name)], 'host' )

    def stop_xterm(self):
        for term in self.terms:
            os.kill( term.pid, signal.SIGKILL )
        cleanUpScreens()

    def get_statistic(self):
        result = self.topo.get_statistics()
        statis = {}
        for end1 in result:
            p1 = self.map2name[end1]
            statis[p1] = {}
            for end2 in result[end1]:
                p2 = self.map2name[end2]
                statis[p1][p2] = {}
                statis[p1][p2]['pkt_recv'] = result[end1][end2]['pkt_recv']
                statis[p1][p2]['pkt_sent'] = result[end1][end2]['pkt_sent']
                statis[p1][p2]['bytes_recv'] = result[end1][end2]['bytes_recv']
                statis[p1][p2]['bytes_sent'] = result[end1][end2]['bytes_sent']

        json_str = json.dumps(statis)
        return json_str


    def process_topo(self):
        net = self.net
        net.start()
        for sw in net.switches:
            # print (sw.name, sw.dpid)
            attr = {}
            attr['type'] = sw.params['type']
            attr['location'] = sw.params['location']
            attr['section'] = sw.params['section']
            attr['id'] = "of:" + sw.dpid
            self.nodes[sw.name] = attr
            self.map2name[attr['id']] = sw.name
            self.switches.append(sw.name)
            # print (sw.name, self.nodes[sw.name])
        for host in net.hosts:
            # print (host.name, host.IP())
            attr = {}
            attr['type'] = host.params['type']
            attr['section'] = host.params['section']
            attr['location'] = host.params['location']
            attr['id'] = host.MAC() + ":None"
            attr['ip'] = host.IP()
            attr['mac'] = host.MAC()
            self.nodes[host.name] = attr
            self.map2name[attr['mac']] = host.name
            self.hosts.append(host.name)
            # print (host.name, self.nodes[host.name])
        for link in net.links:
            self.lines.append(link)
            l = str(link).split("<->")
            p1 = l[0].split('-')
            p2 = l[1].split('-')
            end1 = p1[0]
            end2 = p2[0]
            # print(p1, p2)
            self.nodes[end1][p1[1][3:]] = end2
            self.nodes[end2][p2[1][3:]] = end1
            if end1 not in self.edges:
                self.edges[end1]={}
            if end2 not in self.edges:
                self.edges[end2]={}
            self.edges[end1][end2] = (p1[1], p2[1])
            self.edges[end2][end1] = (p2[1], p1[1])

        # print(self.edges)

        print ("switches num:%d, hosts num:%d, links num:%d" %(len(net.switches), len(net.hosts), len(net.links)))
        self.testall(net)
        
    
    def gen_json2(self, json_path):
        data = []
        section = {}
        for name in self.switches:
            node = self.nodes[name]
            sec = node['section']
            if sec not in section:
                section[sec] = {}
                section[sec]['section'] = sec
                section[sec]['nodes'] = []
                section[sec]['edges'] = []
            attr = {}
            attr['name'] = name
            attr['type'] = node['type']
            attr['location'] = node['location']
            section[sec]['nodes'].append(attr)

        for name in self.hosts:
            node = self.nodes[name]
            sec = node['section']
            if sec not in section:
                section[sec] = {}
                section[sec]['section'] = sec
                section[sec]['nodes'] = []
                section[sec]['edges'] = []
            attr = {}
            attr['name'] = name
            attr['type'] = node['type']
            attr['location'] = node['location']
            attr['ip'] = node['ip']
            attr['mac'] = node['mac']
            # print node['mac']
            section[sec]['nodes'].append(attr)
        

        edge = {}
        region_edge = {}
        region_edge['section'] = 'region_edge'
        region_edge['edges'] = []
        region_edge['nodes'] = []
        for e1 in self.edges:
            edge[e1] = {}
            for e2 in self.edges[e1]:
                edge[e1][e2] = False
        for e1 in self.edges:
            for e2 in self.edges[e1]:
                if edge[e1][e2] == False:
                    s1 = self.nodes[e1]['section']
                    s2 = self.nodes[e2]['section']
                    if s1 == s2:
                        attr = {}
                        attr['source'] = e1
                        attr['target'] = e2
                        edge[e1][e2] = True
                        edge[e2][e1] = True
                        section[s1]['edges'].append(attr)
                    else:
                        attr = {}
                        attr['source'] = e1
                        attr['target'] = e2
                        edge[e1][e2] = True
                        edge[e2][e1] = True
                        region_edge['edges'].append(attr)

        for sec in section:
            data.append(section[sec])
        data.append(region_edge)
        out_f = open(json_path, 'w')
        json.dump(data, out_f, indent = 4)
        json_str = json.dumps(data)
        # print json_str
        return json_str

            
        

    def gen_json(self, json_path):
        data = []
        section = {}
        for name in self.switches:
            node = self.nodes[name]
            sec = node['section']
            if sec not in section:
                section[sec] = {}
                section[sec]['section'] = sec
                section[sec]['nodes'] = []
                section[sec]['edges'] = []
            attr = {}
            attr['name'] = name
            attr['type'] = node['type']
            attr['location'] = node['location']
            section[sec]['nodes'].append(attr)
            
        for name in self.hosts:
            node = self.nodes[name]
            sec = node['section']
            if sec not in section:
                section[sec] = {}
                section[sec]['section'] = sec
                section[sec]['nodes'] = []
                section[sec]['edges'] = []
            attr = {}
            attr['name'] = name
            attr['type'] = node['type']
            attr['location'] = node['location']
            attr['ip'] = node['ip']
            attr['mac'] = node['mac']
            section[sec]['nodes'].append(attr)
        

        edge = {}
        link = {}
        link['section'] = 'edges'
        link['edges'] = []
        link['nodes'] = []
        for e1 in self.edges:
            edge[e1] = {}
            for e2 in self.edges[e1]:
                edge[e1][e2] = False
        for e1 in self.edges:
            for e2 in self.edges[e1]:
                if edge[e1][e2] == False:
                    attr = {}
                    attr['source'] = e1
                    attr['target'] = e2
                    edge[e1][e2] = True
                    edge[e2][e1] = True
                    link['edges'].append(attr)

        for sec in section:
            data.append(section[sec])
        data.append(link)
        out_f = open(json_path, 'w')
        json.dump(data, out_f, indent = 4)
        json_str = json.dumps(data)
        return json_str

            


    def add_host(self, name, cls=None, **params):
        return self.net.addHost(name, cls, **params)

    def add_switch(self, name, cls=None, **params):
        return self.net.addSwitch(name, cls, **params)

    def add_link(self, node1, node2, port1=None, port2=None,
                 cls=None, **params):
        return self.net.addLink(node1, node2, port1, port2,cls, **params)
    
    def testall(self, net):
        hosts = net.hosts
        h_src = hosts[0:2]
        for h1 in h_src:
	        for h2 in hosts:
	            h1.cmd('ping -c 1 %s' % h2.IP())

    def print_map(self):
        for id in self.map2name:
            print(id, self.map2name[id])
    def stop(self):
        self.net.stop()


if __name__ == '__main__':
    controller = Net()
    # controller.net.startTerms()
    # controller.net.stopXterms()
    controller.start_xterm(controller.net.hosts[0].name)
    controller.stop_xterm()
    # controller.cmd_host(controller.net.hosts[0].name, 'ifconfig')
    print (controller.ping_host(controller.net.hosts[0].name,controller.net.hosts[1].name))
    controller.gen_json2('mininet/simulation/topo_new_all.json')
    # controller.print_map()


    CLI(controller.net)
    # controller.topo = topo_get.Topo()
    # controller.topo.print_edges()
        

    out_f = open("statis.json", 'w')
    data = controller.get_statistic()
    json.dump(data,out_f,indent = 4)
    


    
    controller.stop()