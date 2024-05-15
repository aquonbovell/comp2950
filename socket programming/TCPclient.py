"""TCP Client"""
# import socket module
from socket import *

# serverName is the ip address of the server
serverName = 'localhost'
serverPort = 12009

# AF_INET is the address family for IPv4 and SOCK_STREAM is the socket type for TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
# connect to the server
clientSocket.connect((serverName, serverPort))

sentence = input('Input lowercase sentence:')
# can only send bytes, so we need to encode the string to bytes using utf-8 because 
# the computer can only understand 0s and 1s
clientSocket.send(bytes(sentence, 'utf-8'))

print("Sent to Make Upper Case Server Over TCP: ", sentence)

modifiedSentence = clientSocket.recv(1024)

print("Received from Make Upper Case Server Over TCP: ", modifiedSentence.decode('utf-8'))

clientSocket.close()