#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import Node
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import Link, TCLink

def customTopo():
    # Create an empty network
    net = Mininet(controller=Controller, link=TCLink)

    info('* Adding controller\n')
    net.addController('c0')

    info('* Adding routers\n')
    router1 = net.addHost('r1', ip='10.0.0.1/24')
    router2 = net.addHost('r2', ip='10.0.1.1/24')

    info('* Adding switches\n')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')

    info('* Adding hosts\n')
    # Hosts for switch 1
    h1 = net.addHost('h1', ip='10.0.0.2/24')
    h2 = net.addHost('h2', ip='10.0.0.3/24')
    h3 = net.addHost('h3', ip='10.0.0.4/24')
    # Hosts for switch 2
    h4 = net.addHost('h4', ip='10.0.0.5/24')
    h5 = net.addHost('h5', ip='10.0.0.6/24')
    h6 = net.addHost('h6', ip='10.0.0.7/24')
    # Hosts for switch 3
    h7 = net.addHost('h7', ip='10.0.1.2/24')
    h8 = net.addHost('h8', ip='10.0.1.3/24')
    h9 = net.addHost('h9', ip='10.0.1.4/24')
    # Hosts for switch 4
    h10 = net.addHost('h10', ip='10.0.1.5/24')
    h11 = net.addHost('h11', ip='10.0.1.6/24')
    h12 = net.addHost('h12', ip='10.0.1.7/24')

    info('* Creating links\n')
    # Connect the routers to each other
    net.addLink(router1, router2)

    # Connect switches to routers
    net.addLink(router1, s1)
    net.addLink(router1, s2)
    net.addLink(router2, s3)
    net.addLink(router2, s4)

    # Connect hosts to switches
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)

    net.addLink(h4, s2)
    net.addLink(h5, s2)
    net.addLink(h6, s2)

    net.addLink(h7, s3)
    net.addLink(h8, s3)
    net.addLink(h9, s3)

    net.addLink(h10, s4)
    net.addLink(h11, s4)
    net.addLink(h12, s4)

    info('* Starting network\n')
    net.start()

    info('* Configuring router interfaces\n')
    # Setup router1 interfaces
    router1.cmd('ifconfig r1-eth0 10.0.0.1/24')  # Interface connected to router2
    router1.cmd('ifconfig r1-eth1 10.0.0.254/24')  # Interface to switches s1, s2

    # Setup router2 interfaces
    router2.cmd('ifconfig r2-eth0 10.0.1.1/24')  # Interface connected to router1
    router2.cmd('ifconfig r2-eth1 10.0.1.254/24')  # Interface to switches s3, s4

    info('* Enabling IP forwarding on routers\n')
    router1.cmd('sysctl -w net.ipv4.ip_forward=1')
    router2.cmd('sysctl -w net.ipv4.ip_forward=1')

    info('* Configuring routes on hosts\n')
    # Set default routes for hosts to direct traffic to the appropriate router
    h1.cmd('route add default gw 10.0.0.1')
    h2.cmd('route add default gw 10.0.0.1')
    h3.cmd('route add default gw 10.0.0.1')
    h4.cmd('route add default gw 10.0.0.1')
    h5.cmd('route add default gw 10.0.0.1')
    h6.cmd('route add default gw 10.0.0.1')

    h7.cmd('route add default gw 10.0.1.1')
    h8.cmd('route add default gw 10.0.1.1')
    h9.cmd('route add default gw 10.0.1.1')
    h10.cmd('route add default gw 10.0.1.1')
    h11.cmd('route add default gw 10.0.1.1')
    h12.cmd('route add default gw 10.0.1.1')

    info('* Running CLI\n')
    CLI(net)

    info('* Stopping network\n')
    net.stop()

run()
