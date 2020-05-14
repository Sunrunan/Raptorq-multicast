from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI


class MyTopo(Topo):
    "Simple topology example."

    def __init__(self):
        "Create custom topo."

        # Initialize topology
        Topo.__init__(self)

        # Add hosts and switches
        sender = self.addHost('c1')
        switch = self.addSwitch('s1')
	
        receiver1 = self.addHost('h2')
        receiver2 = self.addHost('h3')
        receiver3 = self.addHost('h4')


        # Add links
	
        self.addLink(sender, switch,bw=1)
        self.addLink(switch, receiver1)
        self.addLink(switch, receiver2)
        self.addLink(switch, receiver3)
	self.addLink(sender, switch2)
        self.addLink(switch2, receiver1)
        self.addLink(switch2, receiver2)
        self.addLink(switch2, receiver3)


topos = { 'mytopo': ( lambda: MyTopo() ) }

if __name__ == '__main__':
    setLogLevel('info')
    topo = MyTopo()
    net = Mininet(topo, controller=None)
    #net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=8000)
    net.start()
    dumpNodeConnections(net.hosts)

    CLI(net)
