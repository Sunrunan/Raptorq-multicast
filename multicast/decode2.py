import time
import socket,threading
import os
SENDERIP = '10.0.0.2'
#SENDERIP = '127.0.0.1'
MYPORT = 10000
MYGROUP = '224.0.0.88'
# create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#sock = socket.socket()
# allow multiple sockets to use the same PORT number
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to the port that we know will receive multicast data
#sock.bind((SENDERIP,MYPORT))
sock.bind((MYGROUP,MYPORT))
# tell the kernel that we are a multicast socket
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)
# Tell the kernel that we want to add ourselves to a multicast group
# The address for the multicast group is the third param
status = sock.setsockopt(socket.IPPROTO_IP,
                             socket.IP_ADD_MEMBERSHIP,
                             socket.inet_aton(MYGROUP) + socket.inet_aton(SENDERIP));
sock.setblocking(0)
filename = 'input2/received.txt'
start=time.time()
while 1:
	f=open(filename,'wb')
	f.truncate()
	received_size=0
	file_total_size=0
	cont=0

	while 1:
	    try:
		data,addr=sock.recvfrom(1024)
		f.write(data)
		cont=cont+1
		if data.find('d')>0:
			if data.find('d')<len(data)-2:
				break
	    except socket.error, e:
		pass
	    else:
		fff=1
	f.close()
	count = len(open(filename, 'r').readlines())
	
	print('get file! and the number of symbol is '+str(count))
	
	f.close()
	if(count>128):
		#print('get enough!')
		val=os.system("./libRaptorQ/examples/decode2")
		if val:
			break
		else:
			print('try again!')
	else:
		print('it is not enough!need get again!')
		print('------------------------------------------------------')
end=time.time()
print(end-start)
#ts = time.time()

