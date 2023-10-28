import socket
import sys

HOST = ""

PORT = 9000

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket has been created')

try:
    mySocket.bind((HOST, PORT))
except socket.error as msg:
    print("Binding has failed.Error Code is: 'message' + str(msg[0]) + 'mesage' + msg(1)")
    sys.exit()
print("socket bin is complete. Now we can proceed to make it listen...")
mySocket.listen(10)
print("socket is now listening")
while 1:
    address = mySocket.accept(0)