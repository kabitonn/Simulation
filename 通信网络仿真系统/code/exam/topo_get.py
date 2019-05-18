# coding:utf-8

import requests
import json

ip = "10.0.0.220"
url = "http://%s:8181/onos/v1/" % ip
auth = ('onos', 'rocks')
filepath = "topo.json"

def get_data(url, auth):
    response = requests.get(url,auth = auth)
    data = response.json()
    return data

class Topo(object):
    def __init__(self):
        self.__topo = {}
        self.__devices = {}
        self.__links = []
        self.__hosts = {}
        self.__flows = {}
        self.Nodes = []
        self.Switches = {}
        self.Hosts = {}
        self.Links = []
        self.process_json(filepath)


    def get_topo(self):
        topo_url = url + "topology"
        data = get_data(topo_url, auth)
        self.__topo['devices'] = data['devices']    # switch num
        self.__topo['links'] = data['links']    # link num
        self.__topo['clusters'] = data['clusters']  # cluster num
        for (k,v) in self.__topo.items(): 
            print(k, v, type(v))

    def get_devices(self):
        devices_url = url + "devices"
        data = get_data(devices_url, auth)
        info = data['devices']
        for v in info:
            id = str(v['id'])   # device id
            if id not in self.__devices and v['available'] == True:
                self.__devices[id]={}
            else:
                continue
            self.__devices[id]['role'] = str(v['role'])     # master / none
            self.__devices[id]['hw'] = str(v['hw'])         # Open vSwitch /
            self.__devices[id]['sw'] = str(v['sw'])         # switch version
            self.__devices[id]['serial'] = str(v['serial']) # ovs /
            self.__devices[id]['driver'] = str(v['driver']) # 
            self.__devices[id]['chassisId'] = str(v['chassisId'])
            self.__devices[id]['channelId'] =str(v['annotations']['channelId']) # controller
            self.__devices[id]['managementAddress'] = str(v['annotations']['managementAddress'])    # controller ip
            self.__devices[id]['protocol'] = str(v['annotations']['protocol'])  # openflow protocol version
            self.__devices[id]['lastUpdate'] = str(v['lastUpdate']) 
        for (k,v) in self.__devices.items(): 
            print(k, type(k), v, type(v))
        print("devices num: ", len(self.__devices))

    def get_links(self):
        links_url = url + "links"
        data = get_data(links_url, auth)
        info = data['links']
        for v in info:
            link = {}
            link['src'] = {}
            link['dst'] = {}
            link['type'] = str(v['type'])
            link['state'] = str(v['state'])
            link['src']['device'] = str(v['src']['device'])     # src device id
            link['src']['port'] = str(v['src']['port'])         # src device port
            link['dst']['device'] = str(v['dst']['device'])     # dst device id
            link['dst']['port'] = str(v['dst']['port'])         # dst device port
            self.__links.append(link)
        for v in self.__links:
            print("%s:%s - %s:%s" %(v['src']['device'], v['src']['port'], v['dst']['device'], v['dst']['port']))
        print("links num: ", len(self.__links))
            
    def get_hosts(self):
        hosts_url = url + "hosts"
        data = get_data(hosts_url, auth)
        info = data['hosts']
        for v in info:
            if len(v['ipAddresses']) != 0:          # host ip
                ip = str(v['ipAddresses'][0])
            else:
                continue
            if ip not in self.__hosts:
                self.__hosts[ip] = {}
            else:
                continue
            self.__hosts[ip]['mac'] = str(v['mac']) # host mac
            self.__hosts[ip]['vlan'] = str(v['vlan'])   
            self.__hosts[ip]['elementId'] = str(v['locations'][0]['elementId']) # belong to device id
            self.__hosts[ip]['port'] = str(v['locations'][0]['port'])   # belong to device port
            self.__hosts[ip]['configured'] = v['configured']
        for (k,v) in self.__hosts.items(): 
            print(k, type(k), v, type(v))
        print("hosts num: " ,len(self.__hosts))


    def get_flows(self):
        flow_url = url + "flows"
        data = get_data(flow_url, auth)
        info = data['flows']
        for v in info:
            deviceId = str(v['deviceId'])       # device id
            if deviceId not in self.__flows:
                self.__flows[deviceId] = []
            flow = {}
            flow['id'] = str(v['id'])           # flow id
            flow['appId'] = str(v['appId'])     
            flow['state'] = str(v['state'])     #
            flow['packets'] = v['packets']
            flow['bytes'] = v['bytes']
            flow['priority'] = v['priority']
            flow['instructions'] = []           # 出口指令
            for ins in v['treatment']['instructions']:
                i = {}
                for k1, v1 in ins.items():
                    i[str(k1)] = str(v1)
                flow['instructions'].append(i)

            flow['criteria'] = []               # 匹配规则
            for cri in v['selector']['criteria']:
                c = {}
                for k1, v1 in cri.items():
                    c[str(k1)] = str(v1)
                flow['criteria'].append(c)


            self.__flows[deviceId].append(flow)

        num = 0
        for k,v in self.__flows.items(): 
            print(k)
            for vv in v:
                print(vv)
            num += len(v)
        print("flows num: ", num)
  
    def process_json(self, filepath):
        f = open(filepath, 'r')
        topo_dict = json.load(f)
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
                print(self.Hosts[name])
            if node_type == 'switch' or node_type == 'router':
                self.Switches[name] = attr
                print(self.Switches[name])
            self.Nodes.append(name)
        for edge in edges:
            src = str(edge['source'])
            dst = str(edge['target'])
            link = {'src':src,'dst':dst}
            self.Links.append(link)
            print(link)


if __name__ == "__main__":
    mytopo = Topo()
    mytopo.get_topo()
    mytopo.get_devices()
    mytopo.get_links()
    mytopo.get_hosts()
    mytopo.get_flows()
