#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel

def customTopology():
    net = Mininet(controller=Controller)

    # Add a controller (optional for basic switching)
    net.addController('c0')

    # Create hosts for s1
    h1 = net.addHost('h1', ip='10.0.1.1')
    h2 = net.addHost('h2', ip='10.0.1.2')
    h3 = net.addHost('h3', ip='10.0.1.3')

    # Create hosts for s4
    h4 = net.addHost('h4', ip='10.0.1.4')
    h5 = net.addHost('h5', ip='10.0.1.5')
    h6 = net.addHost('h6', ip='10.0.1.6')

    # Create hosts for s2
    h7 = net.addHost('h7', ip='10.0.1.7')
    h8 = net.addHost('h8', ip='10.0.1.8')
    h9 = net.addHost('h9', ip='10.0.1.9')

    # Create hosts for s6
    h10 = net.addHost('h10', ip='10.0.1.10')
    h11 = net.addHost('h11', ip='10.0.1.11')
    h12 = net.addHost('h12', ip='10.0.1.12')

    # Create switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')  # Central switch
    s4 = net.addSwitch('s4')
    s5 = net.addSwitch('s5')  # Switch connecting s3 to s2 and s6
    s6 = net.addSwitch('s6')
    
    # Set up links between devices
    # Links for s1
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)

    # Links for s4
    net.addLink(h4, s4)
    net.addLink(h5, s4)
    net.addLink(h6, s4)

    # Links for s2
    net.addLink(h7, s2)
    net.addLink(h8, s2)
    net.addLink(h9, s2)

    # Links for s6
    net.addLink(h10, s6)
    net.addLink(h11, s6)
    net.addLink(h12, s6)

    # Connect switches
    net.addLink(s1, s3)  # s1 to s3
    net.addLink(s4, s3)  # s4 to s3
    net.addLink(s3, s5)  # s3 to s5
    net.addLink(s5, s2)  # s5 to s2
    net.addLink(s5, s6)  # s5 to s6

    # Start the network
    net.start()

    # Start the Mininet CLI to interact with the network
    CLI(net)

    # Stop the network when done
    net.stop()
if __name__ == '__main__':
    setLogLevel('info')
    customTopology()
