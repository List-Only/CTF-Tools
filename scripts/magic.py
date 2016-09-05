import socket
import math

def inttostr(a):
	a = int(a)
	out = ""
	for i in range(4):
		out += chr(int(a/((2**8)**i))%(2**8))
	return out[::-1]

UDP_IP = "104.236.16.36"
UDP_PORT = 3050
head = "x"
tail = "xxxxxxxxxxxxxxxxxxxxxxxx\00\00xxxxxxxxxxxxxxxxxxxxxxxx\00\00"


sock = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP
listener = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP
f = open("allprimes.txt")
for line in f:
	#if int(line) > 200:
		#print("penis")
		#break
	st = head + inttostr(line) + tail
	sock.sendto(bytes(st), (UDP_IP, UDP_PORT))
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("127.0.0.1", UDP_PORT))
while True:
	data, addr = listener.recvfrom(1024) # buffer size is 1024 bytes
	print("received message:", data)
