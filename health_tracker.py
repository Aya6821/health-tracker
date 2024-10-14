#!/usr/bin/python

from mininet.topo import Topo
from (link unavailable) import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class Router(Node):
    "A Node with IP forwarding enabled."

    def config(self, **params):
        super(Router, self).config(**params)
        # Enable IP forwarding
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(Router, self).terminate()

class NetworkTopo(Topo):
    "A network topology with 12 hosts, 4 switches, and 2 routers."

    def build(self):
        # Create routers
        router1 = self.addNode('router1', cls=Router)
        router2 = self.addNode('router2', cls=Router)

        # Create switches
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')
        switch4 = self.addSwitch('s4')

        # Create hosts
        host1 = self.addHost('h1', ip='10.0.1.1/24')
        host2 = self.addHost('h2', ip='10.0.1.2/24')
        host3 = self.addHost('h3', ip='10.0.1.3/24')
        host4 = self.addHost('h4', ip='10.0.2.1/24')
        host5 = self.addHost('h5', ip='10.0.2.2/24')
        host6 = self.addHost('h6', ip='10.0.2.3/24')
        host7 = self.addHost('h7', ip='10.0.3.1/24')
        host8 = self.addHost('h8', ip='10.0.3.2/24')
        host9 = self.addHost('h9', ip='10.0.3.3/24')
        host10 = self.addHost('h10', ip='10.0.4.1/24')
        host11 = self.addHost('h11', ip='10.0.4.2/24')
        host12 = self.addHost('h12', ip='10.0.4.3/24')

        # Connect hosts to switches
        self.addLink(host1, switch1)
        self.addLink(host2, switch1)
        self.addLink(host3, switch1)
        self.addLink(host4, switch2)
        self.addLink(host5, switch2)
        self.addLink(host6, switch2)
        self.addLink(host7, switch3)
        self.addLink(host8, switch3)
        self.addLink(host9, switch3)
        self.addLink(host10, switch4)
        self.addLink(host11, switch4)
        self.addLink(host12, switch4)

        # Connect switches to routers
        self.addLink(switch1, router1, intfName1='s1-eth0', intfName2='router1-eth0')
        self.addLink(switch2, router1, intfName1='s2-eth0', intfName2='router1-eth1')
        self.addLink(switch3, router2, intfName1='s3-eth0', intfName2='router2-eth0')
        self.addLink(switch4, router2, intfName1='s4-eth0', intfName2='router2-eth1')
        self.addLink(router1, router2, intfName1='router1-eth2', intfName2='router2-eth2')

def run():
    topo = NetworkTopo()
    net = Mininet(topo=topo)
    net.start()
    info('*** Running CLI\n')
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
