import socket

HOST = ''
PORT = 8000

# http respose
text_content = b'''
HTTP/1.x 200 OK
Content-Type:text/html

<head>
<title>
    my response
</title>
</head>
<html>
    content
    <img src="1.jpg"/>
</html>
'''

pic_content = b'''
HTTP/1.x 200 OK
Content-Type: image/jpg

'''
# add a pic content
with open('1.jpg', 'rb') as f:
    pic_content += f.read()

s = socket.socket()
s.bind((HOST, PORT))

# after socket defined set a infinite
while True:
    s.listen(1)
    sObj, ip = s.accept()
    request = sObj.recv(2048).decode()
    # deal with the request data
    # now this server code will throw excetion when an invalid http request has been received
    method = request.split(' ')[0]
    src = request.split(' ')[1]

    if method == "GET":
        if src == "/1.jpg":
            content = pic_content
        else:
            content = text_content
        print("connected by:", ip)
        print("request is:", request)
        sObj.sendall(content)
    sObj.close()
