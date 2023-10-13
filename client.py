import json
from socket import *

serverName = '127.0.0.1'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)

message = json.dumps({"method": "random","numb1": 1,"numb2": 10})


# print(message)

clientSocket.connect((serverName, serverPort))
clientSocket.send(message.encode())
modifedSentence = clientSocket.recv(1024)
print('From server: ', modifedSentence.decode())
clientSocket.close()

