"""UDP server
Make sentence upper case server using UDP

Aquon Bovell
COMP3365 - Computer Networks
Semester 2
February 7, 2024
"""

# import socket module
from socket import *

# serverPort is the port number the server will listen on
serverPort = 1212

# AF_INET is the address family for IPv4 and SOCK_STREAM is the socket type for UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)
# serverSocket is bound to the serverPort
serverSocket.bind(('', serverPort))

# print the server is ready to receive
print("The server is ready to receive over UDP")

while True:
  # accept the incoming UDP request
  message, address = serverSocket.recvfrom(2048)
  # receive the sentence from the client
  sentence = message.decode('utf-8')
  # print the sentence received from the client
  print("Received from client: ", sentence)
  # make the sentence upper case
  capitalizedSentence = sentence.upper()
  # send the upper case sentence back to the client
  serverSocket.sendto(bytes(capitalizedSentence, 'utf-8'), address)
  # output the upper case sentence
  print("Sent to client: ", capitalizedSentence)