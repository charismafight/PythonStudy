import http.server
import socketserver

HOST = ''
PORT = 8000

server = socketserver.TCPServer((HOST, PORT), http.server.SimpleHTTPRequestHandler)
server.serve_forever()



###################################################cgi httpserver to deal with post  use the cgi to
