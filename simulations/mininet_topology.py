from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.link import TCLink
from mininet.cli import CLI

def custom_topology():
    net = Mininet(controller=RemoteController, link=TCLink)

    # Add controller
    c0 = net.addController('c0', ip='sdn-controller', port=6633)

    # Add switches and hosts
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')
    h3 = net.addHost('h3', ip='10.0.0.3')
    h4 = net.addHost('h4', ip='10.0.0.4')

    # Add links
    net.addLink(h1, s1, bw=10)
    net.addLink(h2, s1, bw=10)
    net.addLink(s1, s2, bw=5)
    net.addLink(h3, s2, bw=10)
    net.addLink(h4, s2, bw=10)

    # Start the network
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    custom_topology()
