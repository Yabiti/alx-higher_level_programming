import socket
import sys

HOST = ""

PORT = 9000

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket has been created")

try:
    socket.Bind((HOST, PORT))
except socket.Error as msg:
    print("Binding has failed. Error Code is: 'message' + str(msg[0]) + 'message' + (msg[1])")

sys.exit()