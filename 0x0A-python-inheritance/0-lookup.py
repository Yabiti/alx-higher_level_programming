import socket
import sys

HOST = ""

PORT = 9000

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("now we started ethical hacking")

try:
    mySocket.bind((HOST, PORT))
except socket.error as msg:
    print("Binding has failed. Error Code is :' + str(msg[10]) + 'message' + msg[1]")