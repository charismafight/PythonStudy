# this file use socketserver package
import socketserver

HOST = ''
PORT = 8000

text_content = b'''
HTTP/1.x 200 OK
Content-Type: text/html

<head>
<title>WOW</title>
</head>
<html>
<p>Wow, Python Server</p>
<IMG src="1.jpg"/>
<form name="input" action="/" method="post">
First name:<input type="text" name="firstname"><br>
<input type="submit" value="Submit">
</form>
</html>
'''

with open('1.jpg', 'rb') as f:
    pic_content = b'''
    HTTP/1.x 200 OK
    Content-Type: image/jpg

    '''
    pic_content += f.read()


# define a class for each request
class TCPHander(socketserver.BaseRequestHandler):
    def handle(self):
        request = self.request.recv(2048)

        print("connected by:", self.client_address)
        print("request is:", self.request)
        method = request.split(' ')[0]
        src = request.split(' ')[1]
        if method=='GET':
            if src == '/1.jpg':
                content = pic_content
            else:
                content = text_content
            self.request.sendall(content)

        if method=='POST':
            form=request.split('\r\n')
            idx=form.index('')
            entry=form[idx:]
            value=entry[-1].split('=')[-1]
            self.request.sendall(text_content+'\n <p>'+value+'</p>')

#bind host&port in class constructor
server=socketserver.TCPServer((HOST,PORT),TCPHander)
#default every 0.5 sec(poll_interval default) instead of while(1)
server.serve_forever()
