import socket
import sys

HOST = ""

PORT = 9090

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket has been created")

try:
    mySocket.bind((HOST, PORT))
except mySocket.error as msg:
    print("Bindin has failed. Error Code as: + str(msg[0] + 'message' + str(msg[1]))")
    sys.exit()
print("binding has created, now let's proceed...")
mySocket.listen(10)
print("now we can listen")

while 1:
    address = mySocket.accept()
    print('connectd with' + address[0] + ";" + str(address[1]))