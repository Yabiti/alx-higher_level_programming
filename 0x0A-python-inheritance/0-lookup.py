import socket
import sys

HOST = ""

PORT = 9090

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket has been created")

try:
    mySocket.bind((HOST, PORT))
except socket.error as msg:
    print("Binding has failed.Error Code as: + str(msg[0] + 'message' (msg[1]))")
    sys.exit()
print("binding has created. now let's make proceed...")
mySocket.listen(10)
print("socket has been created")
while 1:
    address = mySocket.accept()
    print('connected with' + address[0] + ":" + str(address[1]))