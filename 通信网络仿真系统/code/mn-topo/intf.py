#!/usr/bin/python
import re
import sys
from mininet.cli import CLI
from mininet.log import setLogLevel, info, error
from mininet.net import Mininet
from mininet.link import Intf
from mininet.topolib import TreeTopo
from mininet.util import quietRun
from mininet.node import OVSSwitch, OVSController, Controller, RemoteController
from mininet.topo import Topo
import os

class MyTopo( Topo ):
#    "this topo is used for Scheme_1"
    
    def __init__( self ):
        "Create custom topo."
 
        # Initialize topology
        Topo.__init__( self )
 
        # Add hosts 
        h1 = self.addHost( 'h1' , ip="10.0.0.1/24", mac="00:00:00:00:00:01", defaultRoute="via 10.0.0.254")
        h2 = self.addHost( 'h2' , ip="10.0.0.2/24", mac="00:00:00:00:00:02", defaultRoute="via 10.0.0.254")
        h3 = self.addHost( 'h3' , ip="10.0.0.3/24", mac="00:00:00:00:00:03", defaultRoute="via 10.0.0.254")
        h4 = self.addHost( 'h4' , ip="10.0.0.4/24", mac="00:00:00:00:00:04", defaultRoute="via 10.0.0.254")
        
        # Add switches
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
 
        # Add links
        self.addLink( s1, s2 )
        self.addLink( s1, s3 )
        self.addLink( s2, h1 )
        self.addLink( s2, h2 )
        self.addLink( s3, h3 )
        self.addLink( s3, h4 )
#check eth1
def checkIntf( intf ):
    "Make sure intf exists and is not configured."
    if ( ' %s:' % intf ) not in quietRun( 'ip link show' ):
        error( 'Error:', intf, 'does not exist!\n' )
        exit( 1 )
    ips = re.findall( r'\d+\.\d+\.\d+\.\d+', quietRun( 'ifconfig ' + intf ) )
    if ips:
        error( 'Error:', intf, 'has an IP address,'
               'and is probably in use!\n' )
        exit( 1 )
 
if __name__ == '__main__':
    setLogLevel( 'info' )
    os.system('sudo ifconfig eth1 0')
    # try to get hw intf from the command line; by default, use eth1
    intfName = sys.argv[ 1 ] if len( sys.argv ) > 1 else 'eth1'
    info( '*** Connecting to hw intf: %s' % intfName )
 
    info( '*** Checking', intfName, '\n' )
    checkIntf( intfName )
 
    info( '*** Creating network\n' )
    net = Mininet( topo=MyTopo(),controller=None) 
    switch = net.switches[ 0 ] 
    info( '*** Adding hardware interface', intfName, 'to switch', switch.name, '\n' )
    _intf = Intf( intfName, node=switch )
 
    info( '*** Note: you may need to reconfigure the interfaces for '
          'the Mininet hosts:\n', net.hosts, '\n' )
    c0 = RemoteController( 'c0', ip='127.0.0.1', port=6633 )
    net.addController(c0)
    net.start()
    CLI( net )
    net.stop()


