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