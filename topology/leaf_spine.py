"""
Run: sudo mn --custom mytopo.py --topo mytopo --switch ovsk --controller remote --mac --link tc
Topo: 
                 -- h2
          |-- s2 |
c1 -- s1 -|      -- h3
          |-- s3 -- h4
"""

import sys, os, json
from mininet.topo import Topo

def LoadTopo(file_name):
   # Read file
   json_str = ''
   with open(file_name, "r") as file:
       for line in file:
           json_str += line.replace('\n', '').strip()
   # Load JSON 
   topo = json.loads(json_str)
   return topo

class MyTopo( Topo ):
    
    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Load topology from file
        #topo_data = LoadTopo("topo.json")
	topo_data={"node": [ "c1", "s1", "s2", "s3", "h2", "h3", "h4" ], 
 "link": [  {"src": "c1", "dst": "s1", "bw": 10, "delay": "5ms", "p1": 0, "p2": 1}, 
            {"src": "s1", "dst": "s2", "bw": 10, "delay": "5ms", "p1": 2, "p2": 1}, 
            {"src": "s1", "dst": "s3", "bw": 10, "delay": "5ms", "p1": 3, "p2": 1}, 
            {"src": "s2", "dst": "h2", "bw": 10, "delay": "5ms", "p1": 2, "p2": 0}, 
            {"src": "s2", "dst": "h3", "bw": 10, "delay": "5ms", "p1": 2, "p2": 0}, 
            {"src": "s3", "dst": "h4", "bw": 10, "delay": "5ms", "p1": 3, "p2": 0}
         ] 
}
        # Add hosts and switches
        node = {}
        for name in topo_data["node"]:
            if name[0] == 's':
                # Switch
                node[name] = self.addSwitch( str(name) )
            elif name[0] in {'c', 'h'}:
                # Camara or Host
                node[name] = self.addHost( str(name) )
        
        # Add links
        for link_obj in topo_data["link"]:
           # Data mapping
           src = node[ link_obj["src"] ]
           dst = node[ link_obj["dst"] ]
           p1 = link_obj["p1"]
           p2 = link_obj["p2"]
           linkopts = dict( bw = link_obj.setdefault('bw', 10),
                            #delay = link_obj.setdefault('delay', '10ms'),
                            #jitter = link_obj.setdefault('jitter', '10ms'),
                            loss = link_obj.setdefault('loss', 0) )
           # Set link
           #self.addLink( src, dst, port1=p1, port2=p2,**linkopts )
           self.addLink( src, dst,**linkopts )	
	   #self.addLink(src,dst)

topos = { 'mytopo': ( lambda: MyTopo() ) }

