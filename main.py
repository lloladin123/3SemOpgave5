import json
import random
from socket import *
import threading

def handle_client(connectionSocket, addr):
    print(addr[0])
    keep_communicating = True
    operationType = ""
    global num1
    num1 = 0
    global num2 
    num2 = 0

    def chooseNumbers():
            connectionSocket.send("choose a number".encode())
            message = connectionSocket.recv(1024).decode()
            data = json.loads(message)
            global num1
            num1 = data['numb1']
            connectionSocket.send("choose another number".encode())
            message = connectionSocket.recv(1024).decode()
            data = json.loads(message)
            global num2
            num2 = data['numb2']

    while (keep_communicating):
        connectionSocket.send("plz choose an operation random, add, or substract".encode())
        message = connectionSocket.recv(1024).decode()
        print(message)
        data = json.loads(message)
        operationType = data['method']
        if (operationType == "random"):
            connectionSocket.send(message.encode())
            chooseNumbers()
            randomNumber = random.randint(int(num1), int(num2))
            connectionSocket.send(str(randomNumber).encode())
            handle_client(connectionSocket, addr)

        elif (operationType == "add"):
            connectionSocket.send(message.encode())
            chooseNumbers()
            result = int(num1) + int(num2)
            connectionSocket.send(str(result).encode())
            handle_client(connectionSocket, addr)

        elif (operationType == "substract"):
            connectionSocket.send(message.encode())
            chooseNumbers()
            result = int(num1) - int(num2)
            connectionSocket.send(str(result).encode())
            handle_client(connectionSocket, addr)
        elif (operationType == "close"):
            keep_communicating = False
        else:
            connectionSocket.send("Invalid value plz write either random, add or substract".encode())
            handle_client(connectionSocket, addr)

    connectionSocket.close()



serverPort = 12001
serverHost = '127.0.0.1'
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handle_client, args=(connectionSocket, addr)).start()