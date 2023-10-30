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
print("bind has been created, now it hasprocced to listen...")
mySocket.listen(10)
print("socket is now listening")
while 1:
    address = socket.accept()
    print("conected with")
    mySocket.close()
