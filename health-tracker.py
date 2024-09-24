#!/usr/bin/env python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel

class DualNetworkTopo(Topo):
    def build(self):
        # Create the first network components
        s1 = self.addSwitch('s1')
        r1 = self.addHost('r1', ip='10.0.0.1')
        
        h1 = self.addHost('h1', ip='10.0.0.2')
        h2 = self.addHost('h2', ip='10.0.0.3')
        h3 = self.addHost('h3', ip='10.0.0.4')

        # Connect first network's hosts to the switch and router
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)
        self.addLink(s1, r1)

        # Create the second network components
        s2 = self.addSwitch('s2')
        r2 = self.addHost('r2', ip='10.0.1.1')

        h4 = self.addHost('h4', ip='10.0.1.2')
        h5 = self.addHost('h5', ip='10.0.1.3')
        h6 = self.addHost('h6', ip='10.0.1.4')

        # Connect second network's hosts to the switch and router
        self.addLink(h4, s2)
        self.addLink(h5, s2)
        self.addLink(h6, s2)
        self.addLink(s2, r2)

        # Connect the two routers via a wireless link
        self.addLink(r1, r2, cls=WirelessLink, params={'ssid': 'mininet-wifi'})

def run():
    # Set logging level
    setLogLevel('info')

    # Create the network using the DualNetworkTopo
    topo = DualNetworkTopo()
    net = Mininet(topo=topo)
    
    # Start the network
    net.start()
    
    # Open the command line interface
    CLI(net)
    
    # Stop the network when done
    net.stop()

if _name_ == '_main_':
    run()