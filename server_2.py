#!C:/Python27/python

import socket
import thread

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind(('10.9.0.95',8000))
serversocket.listen(1)

clientsocket,clientaddress=serversocket.accept()
print "Connection from -- ",clientaddress