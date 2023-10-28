import socket
import sys

HOST = ""

PORT = 9000

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket has been created")

try:
    socket.BInd((HOST, PORT))
except socket.Error as msg:
    print("Binding has failed.Error Code is: 'message' + str(msg[0]) + 'message' + (msg[1])")
sys.exit()

print("socket has been created, now lets listen")

mySocket.listen(10)
print("socket is now listening")

while 1:
    address = mySocket.accept()
    print('connected with ' + address[0] + ':' + str(address[1]))
mySocket.close()