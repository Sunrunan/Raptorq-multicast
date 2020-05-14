import socket
import os
import time
filename = 'data.txt'
filesize = str(os.path.getsize(filename))
fname1, fname2 = os.path.split(filename)
client_addr = ('127.0.0.1',9999)
f = open(filename,'rb')
count = 0
flag = 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 9999))
while True:
 if count == 0:
  s.send(filesize.encode())
  start = time.time()
  s.recv(1024)
  s.send(fname2.encode())
 for line in f:
  s.send(line)
  print('sending...')
 s.send(b'end')
 break
 
s.close
end = time.time()
print('cost' + str(round(end - start, 2)) + 's')


