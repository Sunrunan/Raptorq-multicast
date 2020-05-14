# Raptorq-multicast
// start ryu 

ryu-manager --verbose --observe-links simple_switch_igmp_13.py ofctl_rest.py rest_topology.py gui_topology/gui_topology.py  

or

ryu-manager --verbose --observe-links simple_switch_igmp_13.py gui_topology/gui_topology.py

//start openvswtich

export PATH=$PATH:/usr/local/share/openvswitch/scripts

ovs-ctl start

//start python custom topology

mn --custom mytopo.py --topo mytopo --mac --controller=remote,ip=127.0.0.1,port=6653 --link tc 


//test link

pingall

//open xterm

xterm c1(s1,s2,s3,h2,h3,h4)

//see flow table

ovs-ofctl dump-flows s1(s2,s3)


//start multicast 

//in xterm c1

python encode.py

//in xterm h2(h3,h4)

python decode2(3,4).py
