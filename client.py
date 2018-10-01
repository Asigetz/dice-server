import socket
import json

data = {'app': 'asaf','throw': 1}
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('localhost', 8875))
clientSocket.sendall(json.dumps(data))
respond = clientSocket.recv(1024)

print('Received', repr(respond))
