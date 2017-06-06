#client side
import socket

#because of only one computer i have so call myself ip
HOSTAdd='127.0.0.1'
PORT=8000

request=b'hello?'

#config socket similar with server side
s=socket.socket()
s.connect((HOSTAdd,PORT))
#TypeError: 'str' does not support the buffer interface
#request here is a str
#in py3 bytes args should set as b'' or manually encode just like i dit in server.py
s.sendall(request)
reply=s.recv(1024)
print('reply is :',reply.decode())
s.close()