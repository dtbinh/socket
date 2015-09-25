#!C:\Python27\python

import socket
#import select

clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('localhost',8000))
clientsocket.settimeout(2)
print "Enter your name"
name=raw_input()
clientsocket.send(name)
while 1:
#	ready_to_read,temp1,temp2=select.select([clientsocket],[],[])
#	if ready_to_read:
#		data=clientsocket.recv()
#		print data
	try:
		data=clientsocket.recv(1024)
		print ""
		print data
	except:
		print ""
		print "No new data available"
	print ""
	data=raw_input('>>> ')
	if not data:
		continue
	if data=="exit":
		clientsocket.send(data)
		break
	clientsocket.send(data)

clientsocket.close()