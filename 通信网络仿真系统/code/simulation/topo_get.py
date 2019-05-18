# coding:utf-8


import requests

ip = "10.0.0.220"
url = "http://%s:8181/onos/v1/" % ip
auth = ('onos', 'rocks')
filepath = "mininet/custom/topo.json"

def get_data(url, auth):
    response = requests.get(url,auth = auth)
    data = response.json()
    return data

class Topo(object):
    def __init__(self):
        self.topo = {}
        self.devices = {}
        self.links = []
        self.hosts = {}
        self.edges = {}
        self.flows = {}
        self.statistics = {}
        self.get_topo()
        self.get_devices()
        self.get_links()
        self.get_hosts()
        
        

    def get_topo(self):
        topo_url = url + "topology"
        data = get_data(topo_url, auth)
        self.topo['devices'] = data['devices']    # switch num
        self.topo['links'] = data['links']    # link num
        self.topo['clusters'] = data['clusters']  # cluster num
        for (k,v) in self.topo.items(): 
            print(k, v)

    def get_devices(self):
        devices_url = url + "devices"
        data = get_data(devices_url, auth)
        info = data['devices']
        for v in info:
            id = str(v['id'])   # device id
            if id not in self.devices and v['available'] == True:
                attr ={}
            else:
                continue
            attr['role'] = str(v['role'])     # master / none
            attr['hw'] = str(v['hw'])         # Open vSwitch /
            attr['sw'] = str(v['sw'])         # switch version
            attr['serial'] = str(v['serial']) # ovs /
            attr['driver'] = str(v['driver']) # 
            attr['chassisId'] = str(v['chassisId'])
            attr['channelId'] =str(v['annotations']['channelId']) # controller
            attr['managementAddress'] = str(v['annotations']['managementAddress'])    # controller ip
            attr['protocol'] = str(v['annotations']['protocol'])  # openflow protocol version
            attr['lastUpdate'] = str(v['lastUpdate']) 
            device_port_url = devices_url + '/' + id +'/ports'
            data = get_data(device_port_url, auth)
            ports = data['ports']
            for p in ports:
                if p['port'] =='local':
                    attr['name'] = str(p['annotations']['portName'])
            self.devices[id] = attr
            self.edges[id] = {}
        # for (k,v) in self.devices.items(): 
        #     print(k, v['name'])
        print("devices num: ", len(self.devices))

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
            link['src']['port'] = int(v['src']['port'])         # src device port
            link['dst']['device'] = str(v['dst']['device'])     # dst device id
            link['dst']['port'] = int(v['dst']['port'])         # dst device port
            self.links.append(link)
            self.edges[link['src']['device']][link['src']['port']] = link['dst']['device']
            self.edges[link['dst']['device']][link['dst']['port']] = link['src']['device']
        # for v in self.links:
        #     print("%s:%s - %s:%s" %(v['src']['device'], v['src']['port'], v['dst']['device'], v['dst']['port']))
        print("links num: ", len(self.links))
            
    def get_hosts(self):
        hosts_url = url + "hosts"
        data = get_data(hosts_url, auth)
        info = data['hosts']
        for v in info:
            mac = str(v['mac'])
            if mac == "":
                continue
            if mac not in self.hosts:
                attr = {}
            else:
                continue
            attr['id'] = str(v['id'])    # host id
            attr['ip'] = str(v['ipAddresses'][0]) # host ip
            attr['vlan'] = str(v['vlan'])   
            attr['elementId'] = str(v['locations'][0]['elementId']) # belong to device id
            attr['port'] = int(v['locations'][0]['port'])   # belong to device port
            attr['configured'] = v['configured']
            self.hosts[mac] = attr
            self.edges[mac] = {}
            self.edges[mac][0] = str(attr['elementId'])

            self.edges[attr['elementId']][attr['port']] = mac
            if attr['id'] == '10:00:00:00:00:22:None':
                print attr['port'],self.edges[attr['elementId']][attr['port']]

        # for (k,v) in self.hosts.items(): 
        #     print(k, v)
        print("hosts num: " ,len(self.hosts))

    def get_statistics(self):
        statistics_url = url + "statistics/ports"
        data = get_data(statistics_url,auth)
        info = data["statistics"]
        statis = {}
        for v in info:
            end1 = str(v['device'])
            ports = v['ports']
            if len(ports) == 0:
                continue
            statis[end1] = {}
            # print end1
            for port in ports:
                print end1, port
                end2 = self.edges[end1][(port['port'])]
                statis[end1][end2] = {}
                statis[end1][end2]['pkt_recv'] = port['packetsReceived']
                statis[end1][end2]['pkt_sent'] = port['packetsSent']
                statis[end1][end2]['bytes_recv'] = port['bytesReceived']
                statis[end1][end2]['bytes_sent'] = port['bytesSent']
        print statis
        return statis

    def print_edges(self):
        for e1 in self.edges:
            for p in self.edges[e1]:
                print e1,p,self.edges[e1][p]


    def get_flows(self):
        flow_url = url + "flows"
        data = get_data(flow_url, auth)
        info = data['flows']
        flow_link = {}
        for v in info:
            deviceId = str(v['deviceId'])       # device id
            if deviceId not in self.flows:
                self.flows[deviceId] = []
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


            self.flows[deviceId].append(flow)

        num = 0
        for k,v in self.flows.items(): 
            print(k)
            for vv in v:
                print(vv)
            num += len(v)
        print("flows num: ", num)
  
if __name__ == "__main__":
    mytopo = Topo()
    
