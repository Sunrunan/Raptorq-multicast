import time
import struct
from socket import *
import os
import stat
MAX_PACK_SIZE = 100
SENDERIP = '10.0.0.1 '  # local ip
#SENDERIP='127.0.0.1'
SENDERPORT = 5566  #local port
MYPORT = 10000  # send data to port
MYGROUP = '224.0.0.88'  # multicast list
MYTTL = 255  # TTL of sending data

#enode file by raptorq
val=os.system("./libRaptorQ/examples/encode")
s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
    
s.bind((SENDERIP,SENDERPORT))
# Set Time-to-live (optional)
ttl_bin = struct.pack('@i', MYTTL)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, ttl_bin)
# add to multicast list
status = s.setsockopt(IPPROTO_IP,
                         IP_ADD_MEMBERSHIP,
                          inet_aton(MYGROUP) + inet_aton(SENDERIP)) 

s.connect((SENDERIP,SENDERPORT))
filename = "output/received.txt"
if os.path.isfile(filename):
    file_size = os.stat(filename).st_size
    s.sendto(str(file_size).encode(),(MYGROUP,MYPORT))

 

 

while True:
    f = open(filename, "rb")
    for line in f:	
	s.sendto(line,(MYGROUP,MYPORT))
	
    
    f.close()
    print('send file!')
    time.sleep(5)

    
