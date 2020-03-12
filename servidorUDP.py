# Servidor UDP
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("localhost", serverPort))
print("Servidor listo para recibir .... ")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("Se ha recibido : ", message)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)
