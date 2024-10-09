#!/usr/bin/env python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI

class MyTopo(Topo):
    def build(self):
        # Create routers
        r1 = self.addSwitch('r1')
        r2 = self.addSwitch('r2')
        
        # Create switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        
        # Create hosts
        hosts = [self.addHost(f'h{i}') for i in range(1, 13)]
        
        # Connect routers to switches
        self.addLink(r1, s1)
        self.addLink(r1, s2)
        self.addLink(r2, s3)
        self.addLink(r2, s4)
        
        # Connect switches to hosts
        for i in range(3):
            self.addLink(s1, hosts[i])    # h1, h2, h3 to s1
            self.addLink(s2, hosts[i + 3]) # h4, h5, h6 to s2
            self.addLink(s3, hosts[i + 6]) # h7, h8, h9 to s3
            self.addLink(s4, hosts[i + 9]) # h10, h11, h12 to s4

def run():
    topo = MyTopo()
    net = Mininet(topo=topo)
    net.start()
    
    # Set IP addresses for routers
    r1 = net.get('r1')
    r2 = net.get('r2')
    
    r1.setIP('192.168.1.1', 24)
    r2.setIP('192.168.2.1', 24)
    
    # Configure hosts IP addresses
    for i in range(1, 13):
        h = net.get(f'h{i}')
        if i <= 6:
            h.setIP(f'192.168.1.{i}', 24)
        else:
            h.setIP(f'192.168.2.{i - 6}', 24)
    
    CLI(net)
    net.stop()

if _name_ == '_main_':
    run()
