"""UDP Client"""
# import socket module
from socket import *

# serverName is the ip address of the server
serverName = 'localhost'
serverPort = 1212

# AF_INET is the address family for IPv4 and SOCK_STREAM is the socket type for UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

sentence = input('Input lowercase sentence:')
# can only send bytes, so we need to encode the string to bytes using utf-8 because 
# the computer can only understand 0s and 1s
clientSocket.sendto(bytes(sentence, 'utf-8'), (serverName, serverPort))

print("Sent to Make Upper Case Server Over UDP: ", sentence)

modifiedSentence, serverAddress = clientSocket.recvfrom(2048)

print("Received from Make Upper Case Server: ", modifiedSentence.decode('utf-8'))

clientSocket.close()