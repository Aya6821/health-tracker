#!/usr/bin/env python

from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import OVSController
from mininet.topo import Topo

# Define the topology class
class healthNetTopo(Topo):
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

        # Main Switch
        s3 = self.addSwitch('s3')

        # Connect the two routers
        self.addLink(r1, s3)
        self.addLink(r2, s3)

# Main function to create and run the network
def run():
    # Set logging level
    setLogLevel('info')

    # Create the network using the healthNetTopo
    topo = healthNetTopo()
    net = Mininet(topo=topo, controller=OVSController)

    # Start the network
    net.start()

    # Get the routers
    r1 = net.get('r1')
    r2 = net.get('r2')

    # Configure router interfaces manually
    r1.cmd('ifconfig r1-eth0 10.0.0.1/24')  # r1 connected to its subnet
    r1.cmd('ifconfig r1-eth1 192.168.1.1/24')  # r1 connected to s3 (central switch)

    r2.cmd('ifconfig r2-eth0 10.0.1.1/24')  # r2 connected to its subnet
    r2.cmd('ifconfig r2-eth1 192.168.1.2/24')  # r2 connected to s3 (central switch)

    # Enable IP forwarding on the routers
    r1.cmd('sysctl -w net.ipv4.ip_forward=1')
    r2.cmd('sysctl -w net.ipv4.ip_forward=1')

    # Add static routes to enable communication between the subnets via s3
    r1.cmd('ip route add 10.0.1.0/24 via 192.168.1.2')  # Route traffic for 10.0.1.0/24 to r2
    r2.cmd('ip route add 10.0.0.0/24 via 192.168.1.1')  # Route traffic for 10.0.0.0/24 to r1

    # Open the command line interface for testing
    CLI(net)

    # Stop the network when done
    net.stop()

run()
