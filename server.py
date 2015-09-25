#!C:/Python27/python

import socket
import thread
from datetime import datetime
clients=[]

def handler(clientsocket,clientaddress):
	print "Connection from -- ", clientaddress
	name=clientsocket.recv(1024)
	clients.append(clientsocket)
	while 1:
		data=clientsocket.recv(1024)
		print name+" --> "+data
		if data=="exit":
			break
		current_time=datetime.now().strftime("%H:%M:%S")
		for i in clients:
			if(i!=clientsocket):
				i.send(name+" --> "+data+"  //  "+current_time+"\n")
			else:
				i.send("You"+" --> "+data+"  //  "+current_time+"\n")

	print "Connection over -- ",name,clientaddress
	clients.remove(clientsocket)
	clientsocket.close()

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind(('localhost',8000))
serversocket.listen(10)

while 1:
	clientsocket,clientaddress=serversocket.accept()
	thread.start_new_thread(handler,(clientsocket,clientaddress))
	
serversocket.close()