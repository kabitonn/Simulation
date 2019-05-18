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
        # 1100: 1-->router order 1-->link order 0-->add nodes(0) or hosts(1)  0--> specific node(0:Switch or Invalid)
        self.add_nodes(wt_1, 'wt_1100%s', num_1)
        self.addLink(wt_1[0], router)
        self.addLink(wt_1[0], wt_1[1])    # node_0 <--> node_1
        self.addLink(wt_1[1], wt_1[2])    # node_1 <--> node_2
        self.addLink(wt_1[2], wt_1[3])    # node_2 <--> node_3
        self.addLink(wt_1[2], wt_1[4])

        self.addLink(wt_1[1], wt_1[5])    # node_1 <--> node_5
        self.addLink(wt_1[5], wt_1[6])    # node_5 <--> node_6
        self.addLink(wt_1[6], wt_1[7])    # node_6 <--> node_7
        # Add hosts connected to each node
        self.add_hosts('wt_1111%s', wt_1[0], 2)    # Add 2  hosts to node_0
        self.add_hosts('wt_1112%s', wt_1[1], 3)    # Add 3  hosts to node_1
        self.add_hosts('wt_1113%s', wt_1[2], 3)    # Add 3  hosts to node_2
        self.add_hosts('wt_1114%s', wt_1[3], 3)    # Add 3  hosts to node_3
        self.add_hosts('wt_1115%s', wt_1[4], 3)    # Add 3  hosts to node_4

        self.add_hosts('wt_1116%s', wt_1[5], 7)    # Add 7  hosts to node_5
        self.add_hosts('wt_1117%s', wt_1[6], 4)    # Add 4  hosts to node_6
        self.add_hosts('wt_1118%s', wt_1[7], 3)    # Add 3  hosts to node_7
       
        # link2: Add 8 nodes and corresponding links between them
        num_2 = 8
        wt_2  = []
        self.add_nodes(wt_2, 'wt_1200%s', num_2)
        self.addLink(wt_2[0], router)
        self.addLink(wt_2[0], wt_2[1])   # node_47 <--> node_48
        self.addLink(wt_2[0], wt_2[2])   # node_47 <--> node_49
        self.addLink(wt_2[2], wt_2[3])   # node_49 <--> node_50
        self.addLink(wt_2[2], wt_2[5])   # node_49 <--> node_52
        self.addLink(wt_2[3], wt_2[4])   # node_50 <--> node_51
        self.addLink(wt_2[4], wt_2[6])   # node_51 <--> node_53
        self.addLink(wt_2[4], wt_2[7])   # node_51 <--> node_54
        # Add hosts connected to each node
        self.add_hosts('wt_1211%s', wt_2[0], 2)    # Add 2   hosts to node_47
        self.add_hosts('wt_1212%s', wt_2[1], 2)    # Add 2   hosts to node_48
        self.add_hosts('wt_1213%s', wt_2[2], 4)    # Add 4   hosts to node_49
        self.add_hosts('wt_1214%s', wt_2[3], 14)   # Add 14  hosts to node_50
        self.add_hosts('wt_1215%s', wt_2[4], 3)    # Add 3  hosts to node_51
        self.add_hosts('wt_1216%s', wt_2[5], 2)    # Add 2  hosts to node_52
        self.add_hosts('wt_1217%s', wt_2[6], 6)    # Add 6  hosts to node_53
        self.add_hosts('wt_1218%s', wt_2[7], 2)    # Add 2  hosts to node_54

        # link3: Add 14 nodes and corresponding links between them
        num_3 = 13
        wt_3  = [] 
        self.add_nodes(wt_3, 'wt_1300%s', num_3)
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
        self.add_hosts('wt_1311%s',  wt_3[0], 2)     # Add 2  hosts to node_33
        self.add_hosts('wt_1312%s',  wt_3[1], 11)    # Add 11 hosts to node_34
        self.add_hosts('wt_1313%s',  wt_3[2], 5)     # Add 5  hosts to node_35
        self.add_hosts('wt_1314%s',  wt_3[3], 5)     # Add 5  hosts to node_36
        self.add_hosts('wt_1315%s',  wt_3[4], 4)     # Add 4  hosts to node_37
        self.add_hosts('wt_1316%s',  wt_3[5], 6)     # Add 6  hosts to node_38
        self.add_hosts('wt_1317%s',  wt_3[6], 10)    # Add 10  hosts to node_39
        self.add_hosts('wt_1318%s',  wt_3[7], 6)     # Add 6  hosts to node_40
        self.add_hosts('wt_1319%s',  wt_3[8], 12)    # Add 12  hosts to node_41
        self.add_hosts('wt_13110%s', wt_3[9], 14)    # Add 14  hosts to node_42
        self.add_hosts('wt_13111%s', wt_3[10], 10)   # Add 10 hosts to node_43
        self.add_hosts('wt_13112%s', wt_3[11], 10)   # Add 10  hosts to node_44
        self.add_hosts('wt_13113%s', wt_3[12], 3)    # Add 3  hosts to node_45

    # Create topos connected to HuangShi-->routers[
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

    def create_hs(self, router):
        # link1: Add 1 node connected to the switch
        num_1 = 1
        hs_1  = []
        self.add_nodes(hs_1, 'hs_7100%s', num_1)     # node_87
        self.addLink(hs_1[0], router)

        # link2: Add 7 nodes and corresponding links between them
        num_2 = 7
        hs_2  = [] 
        self.add_nodes(hs_2, 'hs_7200%s', num_2)
        self.addLink(hs_2[0], router)
        self.addLink(hs_2[0], hs_2[1])               # node_8  <--> node_9
        self.addLink(hs_2[1], hs_2[2])               # node_9  <--> node_10
        self.addLink(hs_2[1], hs_2[3])               # node_9  <--> node_11
        self.addLink(hs_2[1], hs_2[4])               # node_9  <--> node_12
        self.addLink(hs_2[2], hs_2[6])               # node_10 <--> node_14
        self.addLink(hs_2[4], hs_2[5])               # node_12 <--> node_13
        # Add hosts connected to each node
        self.add_hosts('hs_7211%s', hs_2[0], 4)      # Add 4 hosts to node_8
        self.add_hosts('hs_7212%s', hs_2[1], 4)      # Add 4 hosts to node_9
        self.add_hosts('hs_7213%s', hs_2[2], 3)      # Add 3 hosts to node_10
        self.add_hosts('hs_7214%s', hs_2[3], 5)      # Add 5 hosts to node_11
        self.add_hosts('hs_7215%s', hs_2[4], 6)      # Add 6 hosts to node_12
        self.add_hosts('hs_7216%s', hs_2[5], 1)      # Add 1 host  to node_13
        self.add_hosts('hs_7217%s', hs_2[6], 5)      # Add 5 hosts to node_14

        # link3: Add 9 nodes and corresponding links between them
        num_3 = 9
        hs_3  = []
        self.add_nodes(hs_3, 'hs_7300%s', num_3)
        self.addLink(hs_3[0], router)
        self.addLink(hs_3[0], hs_3[1])               # node_16 <--> node_17
        self.addLink(hs_3[0], hs_3[2])               # node_16 <--> node_18
        self.addLink(hs_3[1], hs_3[3])               # node_17 <--> node_19
        self.addLink(hs_3[3], hs_3[4])               # node_19 <--> node_20
        self.addLink(hs_3[3], hs_3[5])               # node_19 <--> node_21
        self.addLink(hs_3[5], hs_3[6])               # node_21 <--> node_22
        self.addLink(hs_3[5], hs_3[7])               # node_21 <--> node_23
        self.addLink(hs_3[5], hs_3[8])               # node_21 <--> node_24
        # Add hosts connected to each node
        self.add_hosts('hs_7311%s', hs_3[0], 4)      # Add 4 hosts to node_16
        self.add_hosts('hs_7312%s', hs_3[1], 4)      # Add 4 hosts to node_17
        self.add_hosts('hs_7313%s', hs_3[2], 3)      # Add 3 hosts to node_18
        self.add_hosts('hs_7314%s', hs_3[3], 5)      # Add 5 hosts to node_19
        self.add_hosts('hs_7315%s', hs_3[4], 3)      # Add 3 hosts to node_20
        self.add_hosts('hs_7316%s', hs_3[5], 2)      # Add 2 hosts to node_21
        self.add_hosts('hs_7317%s', hs_3[6], 4)      # Add 4 hosts to node_22
        self.add_hosts('hs_7318%s', hs_3[7], 5)      # Add 5 hosts to node_23
        self.add_hosts('hs_7319%s', hs_3[8], 5)      # Add 5 hosts to node_24

        # link4: Add 8 nodes and corresponding links between them
        num_4 = 8
        hs_4  = []
        self.add_nodes(hs_4, 'hs_7400%s', num_4)
        self.addLink(hs_4[0], router)
        self.addLink(hs_4[0], hs_4[1])               # node_25 <--> node_26
        self.addLink(hs_4[0], hs_4[2])               # node_25 <--> node_27
        self.addLink(hs_4[0], hs_4[3])               # node_25 <--> node_28
        self.addLink(hs_4[3], hs_4[4])               # node_28 <--> node_29
        self.addLink(hs_4[3], hs_4[5])               # node_28 <--> node_30
        self.addLink(hs_4[3], hs_4[6])               # node_28 <--> node_31
        self.addLink(hs_4[6], hs_4[7])               # node_31 <--> node_32
        # Add hosts connected to each node
        self.add_hosts('hs_7411%s', hs_4[0], 8)       # Add 8  hosts to node_25
        self.add_hosts('hs_7412%s', hs_4[1], 10)      # Add 10 hosts to node_26
        self.add_hosts('hs_7413%s', hs_4[2], 14)      # Add 14 hosts to node_27
        self.add_hosts('hs_7414%s', hs_4[3], 2)       # Add 2  hosts to node_28
        self.add_hosts('hs_7415%s', hs_4[4], 6)       # Add 6  hosts to node_29
        self.add_hosts('hs_7416%s', hs_4[5], 3)       # Add 3  hosts to node_30
        self.add_hosts('hs_7417%s', hs_4[6], 8)       # Add 8  hosts to node_31
        self.add_hosts('hs_7418%s', hs_4[7], 11)       # Add 11 hosts to node_32


        
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
        self.add_hosts('jj2010%s', self.routers[2], 1)

        # Create the topo connected to LinBing-->routers[3]
        self.create_lb(self.routers[3])

        # Add 1 host to Shangzhuang-->routers[4]
        self.add_hosts('sz4010%s', self.routers[4], 1)

        # Add 1 host to DaiTou-->routers[5]
        self.add_hosts('dt5010%s', self.routers[5], 1)

        # Add 1 host to HuShi-->routers[6]
        self.add_hosts('HS6010%s', self.routers[6], 1)

        # Create the topo connected to HuangShi-->routers[7]
        self.create_hs(self.routers[7])

        # Add 1 host to ChangTai-->routers[8]
        self.add_hosts('ct8010%s', self.routers[8], 1)

        # Add 1 host to ZhuangBian-->routers[9]
        self.add_hosts('zb9010%s', self.routers[9], 1)		

        	
def configNet():
	
        mytopo=MyTopo()
        net = Mininet( topo=mytopo,controller=None) 
	
        c0 = RemoteController( 'c0', ip='172.17.0.2', port=6633 )
        net.addController(c0)
        net.start()

        CLI( net )
        net.stop()


if __name__ == '__main__':
        setLogLevel( 'info' )
        configNet()
		