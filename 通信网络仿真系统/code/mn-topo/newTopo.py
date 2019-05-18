#!/usr/bin/python
# -*- coding: utf-8 -*-

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.log import setLogLevel,info,error
from mininet.topo import Topo
from mininet.node import RemoteController
from mininet.node import Controller



class MyTopo(Topo):
    # BaiSha WuTang JinJiang LinBing ShangZhuang Daitou Hushi HuangShi ChangTai ZhuangBian
    #  r1     r2      r3       r4       r5        r6     r7      r8       r9       r10

    # Add 10 routers
    num     = 10
    routers = []

    # Create routers with specific number
    def create_routers(self, routers, num = 1):
        for i in range(num):
            routers.append(self.addSwitch('r000%s' %(i + 1)))
    
    # Add hosts with specific number
    def add_hosts(self, label, router, num = 1):
        for i in range(num):
            host = self.addHost(label %(i + 1))
            self.addLink(host, router)
    # Add nodes with specific number
    def add_nodes(self, nodes, label, num = 1):
        for i in range(num):
            nodes.append(self.addSwitch(label %(i + 1)))

    # Create topos connected to WuTang-->routers[1]
    def create_wt(self, router):
        # link0: Add 1 host to WuTang
        self.add_hosts('wt%s', router, 1)
      
        # link1: Add 8 nodes and corresponding links between them
        num_1  = 8
        wt_1 = []
        # 2100: 2-->router order 1-->link order 0-->add nodes(0) or hosts(1)  0--> specific node(0:Invalid)
        self.add_nodes(wt_1, 'wt_2100%s', num_1)
        self.addLink(wt_1[0], router)
        self.addLink(wt_1[0], wt_1[1])    # node_0 <--> node_1
        self.addLink(wt_1[1], wt_1[2])    # node_1 <--> node_2
        self.addLink(wt_1[2], wt_1[3])    # node_2 <--> node_3
        self.addLink(wt_1[2], wt_1[4])

        self.addLink(wt_1[1], wt_1[5])    # node_1 <--> node_5
        self.addLink(wt_1[5], wt_1[6])    # node_5 <--> node_6
        self.addLink(wt_1[6], wt_1[7])    # node_6 <--> node_7
        # Add hosts connected to each node
        self.add_hosts('wt_2111%s', wt_1[0], 2)    # Add 2  hosts to node_0
        self.add_hosts('wt_2112%s', wt_1[1], 3)    # Add 3  hosts to node_1
        self.add_hosts('wt_2113%s', wt_1[2], 3)    # Add 3  hosts to node_2
        self.add_hosts('wt_2114%s', wt_1[3], 3)    # Add 3  hosts to node_3
        self.add_hosts('wt_2115%s', wt_1[4], 3)    # Add 3  hosts to node_4

        self.add_hosts('wt_2116%s', wt_1[5], 7)    # Add 7  hosts to node_5
        self.add_hosts('wt_2117%s', wt_1[6], 4)    # Add 4  hosts to node_6
        self.add_hosts('wt_2118%s', wt_1[7], 3)    # Add 3  hosts to node_7
       
        # link2: Add 8 nodes and corresponding links between them
        num_2 = 8
        wt_2  = []
        self.add_nodes(wt_2, 'wt_2200%s', num_2)
        self.addLink(wt_2[0], router)
        self.addLink(wt_2[0], wt_2[1])   # node_47 <--> node_48
        self.addLink(wt_2[0], wt_2[2])   # node_47 <--> node_49
        self.addLink(wt_2[2], wt_2[3])   # node_49 <--> node_50
        self.addLink(wt_2[2], wt_2[5])   # node_49 <--> node_52
        self.addLink(wt_2[3], wt_2[4])   # node_50 <--> node_51
        self.addLink(wt_2[4], wt_2[6])   # node_51 <--> node_53
        self.addLink(wt_2[4], wt_2[7])   # node_51 <--> node_54
        # Add hosts connected to each node
        self.add_hosts('wt_2211%s', wt_2[0], 2)    # Add 2   hosts to node_47
        self.add_hosts('wt_2212%s', wt_2[1], 2)    # Add 2   hosts to node_48
        self.add_hosts('wt_2213%s', wt_2[2], 4)    # Add 4   hosts to node_49
        self.add_hosts('wt_2214%s', wt_2[3], 14)   # Add 14  hosts to node_50
        self.add_hosts('wt_2215%s', wt_2[4], 3)    # Add 3  hosts to node_51
        self.add_hosts('wt_2216%s', wt_2[5], 2)    # Add 2  hosts to node_52
        self.add_hosts('wt_2217%s', wt_2[6], 6)    # Add 6  hosts to node_53
        self.add_hosts('wt_2218%s', wt_2[7], 2)    # Add 2  hosts to node_54

        # link3: Add 14 nodes and corresponding links between them
        num_3 = 13
        wt_3  = [] 
        self.add_nodes(wt_3, 'wt_2300%s', num_3)
        self.addLink(wt_3[0], router) 
        self.addLink(wt_3[0],  wt_3[1])   # node_33 <--> node_34
        self.addLink(wt_3[0],  wt_3[2])   # node_33 <--> node_35
        self.addLink(wt_3[0],  wt_3[3])   # node_33 <--> node_36

        self.addLink(wt_3[2],  wt_3[5])   # node_35 <--> node_38
        self.addLink(wt_3[2],  wt_3[6])   # node_35 <--> node_39 
        self.addLink(wt_3[5],  wt_3[7])   # node_38 <--> node_40    
        self.addLink(wt_3[6],  wt_3[8])   # node_39 <--> node_41
        self.addLink(wt_3[7],  wt_3[10])  # node_40 <--> node_43
        self.addLink(wt_3[8],  wt_3[11])  # node_41 <--> node_44
        self.addLink(wt_3[10], wt_3[12])  # node_43 <--> node_45
        self.addLink(wt_3[12], wt_3[9])   # node_45 <--> node_42

        self.addLink(wt_3[3], wt_3[4])    # node_36 <--> node_37
        # Add hosts connected to each node
        self.add_hosts('wt_2311%s',  wt_3[0], 2)     # Add 2  hosts to node_33
        self.add_hosts('wt_2312%s',  wt_3[1], 11)    # Add 11 hosts to node_34
        self.add_hosts('wt_2313%s',  wt_3[2], 5)     # Add 5  hosts to node_35
        self.add_hosts('wt_2314%s',  wt_3[3], 5)     # Add 5  hosts to node_36
        self.add_hosts('wt_2315%s',  wt_3[4], 4)     # Add 4  hosts to node_37
        self.add_hosts('wt_2316%s',  wt_3[5], 6)     # Add 6  hosts to node_38
        self.add_hosts('wt_2317%s',  wt_3[6], 10)    # Add 10  hosts to node_39
        self.add_hosts('wt_2318%s',  wt_3[7], 6)     # Add 6  hosts to node_40
        self.add_hosts('wt_2319%s',  wt_3[8], 12)    # Add 12  hosts to node_41
        self.add_hosts('wt_23110%s', wt_3[9], 14)    # Add 14  hosts to node_42
        self.add_hosts('wt_23111%s', wt_3[10], 10)   # Add 10 hosts to node_43
        self.add_hosts('wt_23112%s', wt_3[11], 10)   # Add 10  hosts to node_44
        self.add_hosts('wt_23113%s', wt_3[12], 3)    # Add 3  hosts to node_45

    def create_lb(self, router):
        # link1: Add 4 nodes and corresponding links between them
        lb_1  = []
        num_1 = 4
        self.add_nodes(lb_1, 'lb_3100%s', num_1)
        self.addLink(lb_1[0], router)
        self.addLink(lb_1[0], lb_1[1])    # node_64<-->node_65
        self.addLink(lb_1[1], lb_1[2])    # node_65<-->node_66
        self.addLink(lb_1[1], lb_1[3])    # node_65<-->node_67
        # Add hosts connected to each node
        self.add_hosts('lb_3111%s', lb_1[0], 6)      # Add 6 hosts to node_64
        self.add_hosts('lb_3112%s', lb_1[1], 4)      # Add 4 hosts to node_65
        self.add_hosts('lb_3113%s', lb_1[2], 1)      # Add 1 host  to node_66
        self.add_hosts('lb_3114%s', lb_1[3], 5)      # Add 5 hosts to node_67

        # link2: Add 6 nodes and corresponding links between them
        num_2 = 6
        lb_2  = []
        self.add_nodes(lb_2, 'lb_3200%s', num_2)
        self.addLink(lb_2[0], router)
        self.addLink(lb_2[0], lb_2[1])    # node_68<-->node_69
        self.addLink(lb_2[1], lb_2[2])    # node_69<-->node_70
        self.addLink(lb_2[1], lb_2[3])    # node_69<-->node_71
        self.addLink(lb_2[2], lb_2[4])    # node_70<-->node_72
        self.addLink(lb_2[2], lb_2[5])    # node_70<-->node_73
        # Add hosts connected to each node
        self.add_hosts('lb_3211%s', lb_2[0], 2)      # Add 2 hosts to node_68
        self.add_hosts('lb_3212%s', lb_2[1], 5)      # Add 5 hosts to node_69
        self.add_hosts('lb_3213%s', lb_2[2], 4)      # Add 4 hosts to node_70
        self.add_hosts('lb_3214%s', lb_2[3], 6)      # Add 6 hosts to node_71
        self.add_hosts('lb_3215%s', lb_2[4], 6)      # Add 6 hosts to node_72
        self.add_hosts('lb_3216%s', lb_2[5], 5)      # Add 5 hosts to node_73

        # link3: Add 9 nodes and corresponding links between them
        num_3 = 9
        lb_3  = []
        self.add_nodes(lb_3, 'lb_3300%s', num_3)
        self.addLink(lb_3[0], router)
        self.addLink(lb_3[0], lb_3[1])    # node_55<-->node_56
        self.addLink(lb_3[1], lb_3[5])    # node_56<-->node_60
        self.addLink(lb_3[1], lb_3[6])    # node_56<-->node_61
        self.addLink(lb_3[5], lb_3[8])    # node_60<-->node_63
        self.addLink(lb_3[6], lb_3[7])    # node_61<-->node_62

        self.addLink(lb_3[0], lb_3[3])    # node_55<-->node_58
        self.addLink(lb_3[3], lb_3[2])    # node_58<-->node_57
        self.addLink(lb_3[3], lb_3[4])    # node_58<-->node_59
        # Add hosts connected to each node
        self.add_hosts('lb_3311%s', lb_3[0], 8)      # Add 8  hosts to node_55
        self.add_hosts('lb_3312%s', lb_3[1], 2)      # Add 2  hosts to node_56
        self.add_hosts('lb_3313%s', lb_3[2], 6)      # Add 6  hosts to node_57
        self.add_hosts('lb_3314%s', lb_3[3], 16)     # Add 16 hosts to node_58
        self.add_hosts('lb_3315%s', lb_3[4], 6)      # Add 6  hosts to node_59
        self.add_hosts('lb_3316%s', lb_3[5], 6)      # Add 6  hosts to node_60
        self.add_hosts('lb_3317%s', lb_3[6], 12)     # Add 12 hosts to node_61
        self.add_hosts('lb_3318%s', lb_3[7], 6)      # Add 6  hosts to node_62
        self.add_hosts('lb_3319%s', lb_3[8], 6)      # Add 6  hosts to node_63

        # link4: Add 12 nodes and corresponding links between them
        num_4 = 12
        lb_4  = []
        self.add_nodes(lb_4, 'lb_3400%s', num_4)
        self.addLink(lb_4[0], router)
        self.addLink(lb_4[0], lb_4[1])      # node_74<-->node_75
        self.addLink(lb_4[1], lb_4[3])      # node_75<-->node_77
        self.addLink(lb_4[3], lb_4[9])      # node_77<-->node_83
        self.addLink(lb_4[9], lb_4[7])      # node_83<-->node_81
        self.addLink(lb_4[7], lb_4[11])     # node_81<-->node_85
        self.addLink(lb_4[9], lb_4[8])      # node_83<-->node_82

        self.addLink(lb_4[0], lb_4[2])      # node_74<-->node_76
        self.addLink(lb_4[2], lb_4[10])     # node_76<-->node_84

        self.addLink(lb_4[0], lb_4[4])      # node_74<-->node_78
        self.addLink(lb_4[4], lb_4[5])      # node_78<-->node_79
        self.addLink(lb_4[4], lb_4[6])      # node_78<-->node_80
        # Add hosts to each node
        self.add_hosts('lb_3411%s', lb_4[0], 3)       # Add 3  hosts to node_74
        self.add_hosts('lb_3412%s', lb_4[1], 1)       # Add 1  hosts to node_75
        self.add_hosts('lb_3413%s', lb_4[2], 4)       # Add 4  hosts to node_76
        self.add_hosts('lb_3414%s', lb_4[3], 10)      # Add 10 hosts to node_77
        self.add_hosts('lb_3415%s', lb_4[4], 4)       # Add 4  hosts to node_78
        self.add_hosts('lb_3416%s', lb_4[5], 5)       # Add 5  hosts to node_79
        self.add_hosts('lb_3417%s', lb_4[6], 5)       # Add 5  hosts to node_80
        self.add_hosts('lb_3418%s', lb_4[7], 7)       # Add 7  hosts to node_81
        self.add_hosts('lb_3419%s', lb_4[8], 5)       # Add 5  hosts to node_82
        self.add_hosts('lb_34110%s', lb_4[9], 1)      # Add 1  hosts to node_83
        self.add_hosts('lb_34111%s', lb_4[10], 1)     # Add 1  hosts to node_84
        self.add_hosts('lb_34112%s', lb_4[11], 2)     # Add 2  hosts to node_85

    def __init__(self):
        Topo.__init__(self)

        self.create_routers(self.routers, self.num)
        # Add links connected to each router
        for i in range(self.num - 1):
            self.addLink(self.routers[i], self.routers[i + 1])
            self.addLink(self.routers[0], self.routers[self.num - 1])

        # Add 1 host to BaiSha-->routers[0]
        self.add_hosts('bs%s', self.routers[0], 1)

        # Create the topo connected to WuTang-->routers[1]
        self.create_wt(self.routers[1])

        # Add 1 host to JinJiang-->routers[2]
        self.add_hosts('lb%s', self.routers[2], 1)

        # Create the topo connected to LinBing-->routers[3]
        self.create_lb(self.routers[3])

        # Add 1 host to Shangzhuang-->routers[4]
        # self.add_hosts('sz%s', self.routers[4], 1)

        # Add 1 host to DaiTou-->routers[5]
        # self.add_hosts('dt%s', self.routers[5], 1)

        # Add 1 host to HuShi-->routers[6]
        # self.add_hosts('hs%s', self.routers[6], 1)

        # Create the topo connected to HuangShi-->routers[7]
        # self.create_hs(self.routers[7])

        # Add 1 host to ChangTai-->routers[8]
        self.add_hosts('ct%s', self.routers[8], 1)

        # Add 1 host to ZhuangBian-->routers[9]
        self.add_hosts('zb%s', self.routers[9], 1)		

        # huangshi = self.addSwitch('s3')
        node_87 = self.addSwitch('node_87')
        host = self.addHost('ctrl_ctr',ip='10.0.12.1/16',mac='10:00:00:00:00:00')
        self.addLink(host,node_87)
        self.addLink(node_87,self.routers[7])
        self.addLink(self.routers[8],self.routers[7])
        self.addLink(self.routers[6],self.routers[7])
		
        node_8 = self.addSwitch('node_8')
        host = self.addHost('s011901a',ip='10.0.11.101/16',mac='10:00:00:00:00:01')
        self.addLink(host,node_8)
        host = self.addHost('s011911a',ip='10.0.11.111/16',mac='10:00:00:00:00:02')
        self.addLink(host,node_8)
        host = self.addHost('s011912a',ip='10.0.11.112/16',mac='10:00:00:00:00:03')
        self.addLink(host,node_8)
        host = self.addHost('m011000b',ip='10.0.11.20/16',mac='10:00:00:00:00:04')
        self.addLink(node_8,self.routers[7])		

        node_9 = self.addSwitch('node_9')
        host = self.addHost('s011901',ip='10.0.11.91/16',mac='10:00:00:00:00:05')
        self.addLink(host,node_9)
        host = self.addHost('s011001a',ip='10.0.11.11/16',mac='10:00:00:00:00:06')
        self.addLink(host,node_9)
        host = self.addHost('s011027',ip='10.0.11.27/16',mac='10:00:00:00:00:07')
        self.addLink(host,node_9)
        host = self.addHost('s011023',ip='10.0.11.23/16',mac='10:00:00:00:00:08')
        self.addLink(host,node_9)
        self.addLink(node_8,node_9)
		
        node_10 = self.addSwitch('node_10')
        host = self.addHost('s011001',ip='10.0.11.1/16',mac='10:00:00:00:00:09')
        self.addLink(host,node_10)
        host = self.addHost('s011012',ip='10.0.11.12/16',mac='10:00:00:00:00:10')
        self.addLink(host,node_10)
        host = self.addHost('s011010',ip='10.0.11.10/16',mac='10:00:00:00:00:11')
        self.addLink(host,node_10)
        self.addLink(node_9,node_10)
		
        node_11 = self.addSwitch('node_11')
        host = self.addHost('s011911c',ip='10.0.11.131/16',mac='10:00:00:00:00:12')
        self.addLink(host,node_11)
        host = self.addHost('s011912c',ip='10.0.11.132/16',mac='10:00:00:00:00:13')
        self.addLink(host,node_11)
        host = self.addHost('s011025',ip='10.0.11.25/16',mac='10:00:00:00:00:14')
        self.addLink(host,node_11)
        host = self.addHost('s0119144',ip='10.0.11.144/16',mac='10:00:00:00:00:15')
        self.addLink(host,node_11)
        host = self.addHost('m011000d',ip='10.0.11.40/16',mac='10:00:00:00:00:16')
        self.addLink(host,node_11)
        self.addLink(node_9,node_11)
		
        node_12 = self.addSwitch('node_12')
        host = self.addHost('s011310',ip='10.0.11.41/16',mac='10:00:00:00:00:17')
        self.addLink(host,node_12)
        host = self.addHost('s011319',ip='10.0.11.49/16',mac='10:00:00:00:00:18')
        self.addLink(host,node_12)
        host = self.addHost('s011329',ip='10.0.11.59/16',mac='10:00:00:00:00:19')
        self.addLink(host,node_12)
        host = self.addHost('s011339',ip='10.0.11.69/16',mac='10:00:00:00:00:20')
        self.addLink(host,node_12)
        host = self.addHost('s011015',ip='10.0.11.15/16',mac='10:00:00:00:00:21')
        self.addLink(host,node_12)
        host = self.addHost('m011000a',ip='10.0.11.10/16',mac='10:00:00:00:00:22')
        self.addLink(host,node_12)
        self.addLink(node_9,node_12)
		
        node_13 = self.addSwitch('node_13')
        host = self.addHost('s011003',ip='10.0.11.3/16',mac='10:00:00:00:00:23')
        self.addLink(host,node_13)
        self.addLink(node_12,node_13)
		
        node_14 = self.addSwitch('node_14')
        host = self.addHost('s011901b',ip='10.0.11.111/16',mac='10:00:00:00:00:24')
        self.addLink(host,node_14)
        host = self.addHost('s011911b',ip='10.0.11.121/16',mac='10:00:00:00:00:25')
        self.addLink(host,node_14)
        host = self.addHost('s011912b',ip='10.0.11.122/16',mac='10:00:00:00:00:26')
        self.addLink(host,node_14)
        host = self.addHost('s011913b',ip='10.0.11.123/16',mac='10:00:00:00:00:27')
        self.addLink(host,node_14)
        self.addLink(node_10,node_14)

        node_25 = self.addSwitch('node_25')
        hosts = [ self.addHost('s0250'+str(i),ip='10.0.25.'+str(i),mac='10:00:00:00:00:'+str(i)) for i in range(29,36) ]
        for i in range(len(hosts)):
            self.addLink(hosts[i],node_25)
        host = self.addHost('m025104',ip='10.0.25.14/16',mac='10:00:00:00:00:36')
        self .addLink(host,node_25)
        self.addLink(node_25,self.routers[7])
		
        node_26 = self.addSwitch('node_26')
        hosts = [ self.addHost('s0250'+str(i),ip='10.0.25.'+str(i),mac='10:00:00:00:00:'+str(i+22)) for i in range(15,24) ]
        for i in range(len(hosts)):
            self.addLink(hosts[i],node_26)
        host = self.addHost('s025026',ip='10.0.25.26/16',mac='10:00:00:00:00:46')
        self.addLink(host,node_26)
        host = self.addHost('m025103',ip='10.0.25.13/16',mac='10:00:00:00:00:47')
        self.addLink(host,node_26)
        self.addLink(node_25,node_26)

        node_27 = self.addSwitch('node_27')
        hosts = [ self.addHost('s02500'+str(i),ip='10.0.25.'+str(i),mac='10:00:00:00:00:'+str(i+47)) for i in [*range(1,8), *range(10,14), *range(24,26)]]
        for i in range(len(hosts)):
            self.addLink(hosts[i],node_27)
        host = self.addHost('m025101',ip='10.0.25.11/16',mac='10:00:00:00:00:60')
        self.addLink(host,node_27)
        self.addLink(node_25,node_27)

        node_28 = self.addSwitch('node_28')
        host = self.addHost('s025052',ip='10.0.25.52/16',mac='10:00:00:00:00:61')
        self.addLink(host,node_28)
        host = self.addHost('s025107',ip='10.0.25.17/16',mac='10:00:00:00:00:62')
        self.addLink(host,node_27)
        self.addLink(node_25,node_28)

        node_29 = self.addSwitch('node_29')
        hosts = [ self.addHost('s02500'+str(i),ip='10.0.25.'+str(i),mac='10:00:00:00:00:'+str(i+4)) for i in range(59,64) ]
        for i in range(len(hosts)):
            self.addLink(hosts[i],node_29)
        host = self.addHost('m025108',ip='10.0.25.18/16',mac='10:00:00:00:00:69')
        self.addLink(host,node_29)
        self.addLink(node_28,node_29)
		
        node_30 = self.addSwitch('node_30')
        hosts = [ self.addHost('s02500'+str(i),ip='10.0.25.'+str(i),mac='10:00:00:00:00:'+str(i+15)) for i in range(55,58) ]
        for i in range(len(hosts)):
            self.addLink(hosts[i],node_30)
        self.addLink(node_28,node_30)

        node_31 = self.addSwitch('node_31')
        hosts = [ self.addHost('s02500'+str(i),ip='10.0.25.'+str(i),mac='10:00:00:00:00:'+str(i+35)) for i in range(38,46) ]
        for i in range(len(hosts)):
            self.addLink(hosts[i],node_31)
        host = self.addHost('m025105',ip='10.0.25.15/16',mac='10:00:00:00:00:81')
        self.addLink(host,node_29)
        self.addLink(node_28,node_31)

        node_32 = self.addSwitch('node_32')
        hosts = [ self.addHost('s02500'+str(i),ip='10.0.25.'+str(i),mac='10:00:00:00:00:'+str(i+46)) for i in [*range(47,50),53,54,36,48]]
        for i in range(len(hosts)):
            self.addLink(hosts[i],node_32)
        hosts = [ self.addHost('s02500'+str(i),ip='10.0.25.'+str(i),mac='10:00:00:00:00:a'+str(i-64)) for i in [64,65] ]
        for i in range(len(hosts)):
            self.addLink(hosts[i],node_32)
        host = self.addHost('m025106',ip='10.0.25.16/16',mac='10:00:00:00:00:a2')
        self.addLink(host,node_32)
        self.addLink(node_32,node_31)
		
        node_16 = self.addSwitch('node_16')
        hosts = [ self.addHost('s01200'+str(i),ip='10.0.12.'+str(i),mac='10:00:00:00:01:'+str(i)) for i in [11,12,21,28] ]
        for i in range(len(hosts)):
            self.addLink(hosts[i],node_16)
        self.addLink(node_16,self.routers[7])

        node_17 = self.addSwitch('node_17')
        host = self.addHost('s012029',ip='10.0.12.29/16',mac='10:00:00:00:01:29')
        self.addLink(host,node_17)
        host = self.addHost('s012912',ip='10.0.12.112/16',mac='10:00:00:00:01:ac')
        self.addLink(host,node_17)
        host = self.addHost('s12911',ip='10.0.12.111/16',mac='10:00:00:00:01:ab')
        self.addLink(host,node_17)
        host = self.addHost('m1012001',ip='10.0.12.101/16',mac='10:00:00:00:01:a1')
        self.addLink(host,node_17)
        self.addLink(node_16,node_17)

        node_18 = self.addSwitch('node_18')
        host = self.addHost('s01201',ip='10.0.12.10/16',mac='10:00:00:00:01:10')
        self.addLink(host,node_18)
        host = self.addHost('s012144',ip='10.0.12.54/16',mac='10:00:00:00:01:54')
        self.addLink(host,node_18)
        host = self.addHost('s012442',ip='10.0.12.82/16',mac='10:00:00:00:01:82')
        self.addLink(host,node_18)
        self.addLink(node_16,node_18)

        node_19 = self.addSwitch('node_19')
        host = self.addHost('s012004',ip='10.0.12.4/16',mac='10:00:00:00:01:04')
        self.addLink(host,node_19)
        host = self.addHost('s012005',ip='10.0.12.5/16',mac='10:00:00:00:01:05')
        self.addLink(host,node_19)
        host = self.addHost('s129023',ip='10.0.12.23/16',mac='10:00:00:00:01:23')
        self.addLink(host,node_19)
        host = self.addHost('s012610',ip='10.0.12.70/16',mac='10:00:00:00:01:70')
        self.addLink(host,node_17)
        self.addLink(node_19,node_17)
		
        node_20 = self.addSwitch('node_20')
        host = self.addHost('s012002',ip='10.0.12.2/16',mac='10:00:00:00:01:02')
        self.addLink(host,node_20)
        host = self.addHost('s0129011',ip='10.0.12.11/16',mac='10:00:00:00:01:11')
        self.addLink(host,node_20)
        host = self.addHost('s0129112',ip='10.0.12.22/16',mac='10:00:00:00:01:22')
        self.addLink(host,node_20)
        self.addLink(node_19,node_20)
		
        node_21 = self.addSwitch('node_21')
        host = self.addHost('s0120031',ip='10.0.12.31/16',mac='10:00:00:00:01:31')
        self.addLink(host,node_21)
        host = self.addHost('m1012003',ip='10.0.12.103/16',mac='10:00:00:00:01:a3')
        self.addLink(host,node_21)
        self.addLink(node_19,node_21)

        node_22 = self.addSwitch('node_22')
        host = self.addHost('s0129111',ip='10.0.12.21/16',mac='10:00:00:00:01:21')
        self.addLink(host,node_22)
        host = self.addHost('s0129121',ip='10.0.12.31/16',mac='10:00:00:00:01:31')
        self.addLink(host,node_22)
        host = self.addHost('s012003',ip='10.0.12.3/16',mac='10:00:00:00:01:03')
        self.addLink(host,node_22)
        host = self.addHost('m1012004',ip='10.0.12.104/16',mac='10:00:00:00:01:a4')
        self.addLink(host,node_22)
        self.addLink(node_21,node_22)
		
        node_23 = self.addSwitch('node_23')
        host = self.addHost('s012035',ip='10.0.12.35/16',mac='10:00:00:00:01:35')
        self.addLink(host,node_23)
        host = self.addHost('s012911',ip='10.0.12.101/16',mac='10:00:00:00:01:b1')
        self.addLink(host,node_23)
        host = self.addHost('s0129128',ip='10.0.12.38/16',mac='10:00:00:00:01:38')
        self.addLink(host,node_23)
        host = self.addHost('s0129018',ip='10.0.12.18/16',mac='10:00:00:00:01:18')
        self.addLink(host,node_23)
        host = self.addHost('m1012002',ip='10.0.12.102/16',mac='10:00:00:00:01:a2')
        self.addLink(host,node_22)
        self.addLink(node_21,node_23)
		
        node_24 = self.addSwitch('node_24')
        host = self.addHost('s012041',ip='10.0.12.41/16',mac='10:00:00:00:01:41')
        self.addLink(host,node_24)
        host = self.addHost('s012042',ip='10.0.12.42/16',mac='10:00:00:00:01:42')
        self.addLink(host,node_24)
        host = self.addHost('s0129461',ip='10.0.12.131/16',mac='10:00:00:00:01:d1')
        self.addLink(host,node_24)
        host = self.addHost('s012001',ip='10.0.12.141/16',mac='10:00:00:00:01:e1')
        self.addLink(host,node_24)
        host = self.addHost('m1012005',ip='10.0.12.105/16',mac='10:00:00:00:01:a5')
        self.addLink(host,node_24)
        self.addLink(node_21,node_24)
		
def configNet():
	
        mytopo=MyTopo()
        net = Mininet( topo=mytopo,controller=None) 
	
        c0 = RemoteController( 'c0', ip='127.0.0.1', port=6633 )
        net.addController(c0)
        net.start()

        CLI( net )
        net.stop()



if __name__ == '__main__':
        setLogLevel( 'info' )
        configNet()
		
		
	
