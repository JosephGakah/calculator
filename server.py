import http.server
import socketserver
from http.server import HTTPServer
from handler import MyHandler 

HOST_NAME = 'localhost'
PORT_NUMBER = 8080

server_class = HTTPServer
httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
# print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass