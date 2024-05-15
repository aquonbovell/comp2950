"""Program B is the program that receives the encrypted data and key from program A and decrypts the data using the key. 
It then prints the decrypted data to the console."""
# import socket module
from socket import *

from cypher import decrypt

# serverName is the ip address of the server
serverName = 'localhost'
person_2_port_data = 2501

# AF_INET is the address family for IPv4 and SOCK_STREAM is the socket type for TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
# connect to the server
clientSocket.connect((serverName, person_2_port_data))

print("Received text from friend")

# open a binary file to write the data to
with open('Biden.dat', 'wb') as encryptedFile:
  # read the data from the server
  while True:
    # read the data from the server in 4096 byte chunks
    read_data = clientSocket.recv(4096)
    # if there is no data, close the file and break out of the loop
    if not read_data:
      encryptedFile.close()
      break
    # write the data to the file
    encryptedFile.write(read_data)

clientSocket.close()

person_2_port_data = 2500

# AF_INET is the address family for IPv4 and SOCK_STREAM is the socket type for TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
# connect to the server
clientSocket.connect((serverName, person_2_port_data))

secretKey = b''
# read the key from the server
while True:
  # read the key from the server in 4096 byte chunks
  secretKey_bytes = clientSocket.recv(4096)
  # if there is no data, break out of the loop
  if not secretKey_bytes:
    break
  # append the data to the secretKey
  secretKey += secretKey_bytes

encryptedKey = secretKey.decode('utf-8')
clientSocket.close()

print("Received key from friend")

# read the data from the file and decrypt it
with open('Biden.dat', 'rb') as file:
  # decrypt the key
  key = decrypt(encryptedKey, 4)
  # read the data from the file
  data = file.read()
  # decode the data
  data = data.decode('utf-8')
  Text = ""
  # xor the data with the key to get the original text in binary
  for i in range(len(data)):
    Text += str(int(data[i]) ^ int(key[i]))
  # convert the binary to ascii and then print it
  for i in range(0, len(Text), 8):
    print(chr(int(Text[i:i+8], 2)), end="")