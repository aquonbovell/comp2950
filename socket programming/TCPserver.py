"""TCP server
Make sentence upper case server using TCP

Aquon Bovell
COMP3365 - Computer Networks
Semester 2
February 7, 2024
"""

# import socket module
from socket import *

# serverPort is the port number the server will listen on
serverPort = 12009

# AF_INET is the address family for IPv4 and SOCK_STREAM is the socket type for TCP
serverSocket = socket(AF_INET, SOCK_STREAM)
# serverSocket is bound to the serverPort
serverSocket.bind(('', serverPort))

# serverSocket will listen for incoming TCP requests
serverSocket.listen(1)

# print the server is ready to receive
print("The server is ready to receive over TCP")

while True:
  # accept the incoming TCP request
  conn, addr = serverSocket.accept()
  # receive the sentence from the client
  sentence = conn.recv(1024).decode('utf-8')
  # print the sentence received from the client
  print("Received from client: ", sentence)
  # make the sentence upper case
  capitalizedSentence = sentence.upper()
  # send the upper case sentence back to the client
  conn.send(bytes(capitalizedSentence, 'utf-8'))
  # close the connection
  conn.close()