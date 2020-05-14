import time
import struct
from socket import *

#SENDERIP = '10.0.0.1 '  # local ip
SENDERIP = '127.0.0.1'
SENDERPORT = 5566  #local port
MYPORT = 10000  # send data to port
MYGROUP = '224.0.0.88'  # multicast list
MYTTL = 255  # TTL of sending data


def sender():
    s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)

    s.bind((SENDERIP,SENDERPORT))
    # Set Time-to-live (optional)
    ttl_bin = struct.pack('@i', MYTTL)
    s.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, ttl_bin)
    # add to multicast list
    status = s.setsockopt(IPPROTO_IP,
                          IP_ADD_MEMBERSHIP,
                          inet_aton(MYGROUP) + inet_aton(SENDERIP))  
    while True:
        data = 1
        s.sendto(data, (MYGROUP,MYPORT))
        print "send data ok !"
        time.sleep(10)


if __name__ == "__main__":
    sender()
