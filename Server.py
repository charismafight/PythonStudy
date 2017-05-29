# for server side
import socket

HOST = ''
PORT = 8000

reply = 'Yes'

#default ipv4=AF_INET  tcp
s = socket.socket()
s.bind((HOST, PORT))

# passively wait max 3 connection of queue
s.listen(3)
# return a socket and address info
sObj, address = s.accept()
#max buffersize bytes
request =sObj.recv(1024)

print('request is :',request)
print('connected by :',address)


#send msg
#now in python3 send an senall func can only receive encode str,means receive bytes args
sObj.sendall(reply.encode("utf-8"))
#close
sObj.close()

