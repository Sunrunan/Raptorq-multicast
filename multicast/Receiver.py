import sys
import struct
import time
import socket

# 
#if "linux" in sys.platform:
    # 
    #nic_name = "eth0"
    # 
    #mcast_group_ip = "239.255.255.252"
#else:
    #mcast_group_ip = socket.gethostbyname(socket.gethostname())
mcast_group_ip = "239.255.255.252"
mcast_group_port = 23456

def receiver():
    # 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    # 
    #if "linux" in sys.platform:
        #sock.setsockopt(socket.SOL_SOCKET, 25, nic_name)
    # 
    sock.bind((mcast_group_ip, mcast_group_port))
    # 
    mreq = struct.pack("=4sl", socket.inet_aton(mcast_group_ip), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)

    # 
    # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 
    # sock.setblocking(0)
    while True:
        try:
            message, addr = sock.recvfrom(1024)
            print(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}: Receive data from {addr}: {message.decode()}')
        except :
            print("while receive message error occur")


if __name__ == "__main__":
    receiver()



