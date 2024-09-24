#!/usr/bin/env python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel
#from mininet.link import Link, WirelessLink

class WirelessDualNetworkTopo(Topo):
    def build(self):
        # Create routers
        r1 = self.addHost('r1', ip='10.0.0.1')
        r2 = self.addHost('r2', ip='10.0.1.1')

        # Create switches and hosts for the first router
        s1a = self.addSwitch('s1a')
        s1b = self.addSwitch('s1b')

        h1 = self.addHost('h1', ip='10.0.0.2')
        h2 = self.addHost('h2', ip='10.0.0.3')
        h3 = self.addHost('h3', ip='10.0.0.4')

        h4 = self.addHost('h4', ip='10.0.0.5')
        h5 = self.addHost('h5', ip='10.0.0.6')
        h6 = self.addHost('h6', ip='10.0.0.7')

        # Connect first router to its switches
        self.addLink(s1a, r1)
        self.addLink(s1b, r1)

        # Connect hosts to the first switch of the first router
        self.addLink(h1, s1a)
        self.addLink(h2, s1a)
        self.addLink(h3, s1a)

        # Connect hosts to the second switch of the first router
        self.addLink(h4, s1b)
        self.addLink(h5, s1b)
        self.addLink(h6, s1b)

        # Create switches and hosts for the second router
        s2a = self.addSwitch('s2a')
        s2b = self.addSwitch('s2b')

        h7 = self.addHost('h7', ip='10.0.1.2')
        h8 = self.addHost('h8', ip='10.0.1.3')
        h9 = self.addHost('h9', ip='10.0.1.4')

        h10 = self.addHost('h10', ip='10.0.1.5')
        h11 = self.addHost('h11', ip='10.0.1.6')
        h12 = self.addHost('h12', ip='10.0.1.7')

        # Connect second router to its switches
        self.addLink(s2a, r2)
        self.addLink(s2b, r2)

        # Connect hosts to the first switch of the second router
        self.addLink(h7, s2a)
        self.addLink(h8, s2a)
        self.addLink(h9, s2a)

        # Connect hosts to the second switch of the second router
        self.addLink(h10, s2b)
        self.addLink(h11, s2b)
        self.addLink(h12, s2b)

        # Connect the two routers wirelessly
        #self.addLink(r1, r2, cls=WirelessLink, params={'ssid': 'mininet-wifi'})

        self.addLink(r1,r2) #Physical link
def run():
    # Set logging level
    setLogLevel('info')

    # Create the network using the WirelessDualNetworkTopo
    topo = WirelessDualNetworkTopo()
    net = Mininet(topo=topo)
    
    # Start the network
    net.start()
    
    # Open the command line interface
    CLI(net)
    
    # Stop the network when done
    net.stop()
run()
