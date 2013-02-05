
import time
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP


data = ''
while True :

    data = "k,5,5,5\n"
    sock.sendto(data, (UDP_IP, UDP_PORT))
    time.sleep(.1)
