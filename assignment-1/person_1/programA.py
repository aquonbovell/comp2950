"""Program A encrypts a file using a one-time pad and sends the encrypted file and the encrypted key to Program B using TCP. 
    Program A listens on port 2501 for the file and on port 2500 for the key. The file is encrypted using a one-time 
    pad and the key is encrypted using the Caesar cipher."""
from cypher import encrypt

def generateOTPKey(length):
  import random
  key = ""
  for _ in range(length):
    key += str(random.randint(0,1))
  return key

with open('SleepyBiden.dat', 'r') as file:
  data = file.read()
  # convert the data to binary
  bin_stream = ''.join(format(ord(i), '08b') for i in data)
  # generate a key for the OTP
  key = generateOTPKey(len(bin_stream))
  # encrypt the key
  encryptedKey = encrypt(key, 4)
  encryptedText = ""
  # encrypt the data
  for i in range(len(bin_stream)):
    encryptedText += str(int(bin_stream[i]) ^ int(key[i]))
  # write the encrypted data to a file
  with open('Biden.dat', 'wb') as encryptedFile:
    encryptedFile.write(bytes(encryptedText, 'utf-8'))
    encryptedFile.close()
  file.close()
# import socket module
from socket import *

# person_1_port_data is the port number the server will listen on
person_1_port_data = 2501

# AF_INET is the address family for IPv4 and SOCK_STREAM is the socket type for TCP
serverSocket = socket(AF_INET, SOCK_STREAM)
# serverSocket is bound to the person_1_port_data
serverSocket.bind(('', person_1_port_data))

# serverSocket will listen for incoming TCP requests
serverSocket.listen(1)

# print the server is ready to send
print("The server is ready to send the file")

# accept the incoming TCP request
conn, addr = serverSocket.accept()
# send the upper case sentence back to the client
with open('Biden.dat', 'rb') as file:
  # read the file in 4096 byte chunks
  while True:
    data_bytes = file.read(4096)
    # if there is no data left to read, break the loop
    if not data_bytes:
      break
    # send the data to the client
    conn.send(data_bytes)
# close the connection
conn.close()

# person_1_port_key is the port number the server will listen on
person_1_port_key = 2500

# AF_INET is the address family for IPv4 and SOCK_STREAM is the socket type for TCP
serverSocket = socket(AF_INET, SOCK_STREAM)
# serverSocket is bound to the person_1_port_key
serverSocket.bind(('', person_1_port_key))

# serverSocket will listen for incoming TCP requests
serverSocket.listen(1)

# print the server is ready to send
print("The server is ready to send key")

# accept the incoming TCP request
conn, addr = serverSocket.accept()
# send the encrypted key to the client
# count is used to keep track of the number of 4096 byte chunks sent
count = 1

BUFFSIZE = 4096
while True:
  # break the encrypted key into 4096 byte chunks
  encryptedKey_bytes = encryptedKey[ (count - 1) * BUFFSIZE : count * BUFFSIZE ]
  # if there is no data left to read, break the loop
  if not encryptedKey_bytes:
    break
  # send the data to the client
  conn.send(encryptedKey_bytes.encode('utf-8'))
  # increment the count
  count += 1
# close the connection
conn.close()
