# Part 2 - Program A
import random
from socket import *
from Part1 import encrypt

# Function used to generate an OTP key
def generateOTPKey(message):
    return  "".join(str(random.randint(0, 1)) for _ in range(len(message)))

# Modified encrypt function to handle OTP Encryption
def otpEncrypt(message, key):
    ciphertext = bytearray()
    for i in range(len(message)):                                       
        ciphertext.append(message[i] ^ int(key[i]))
    return ciphertext

# Reads the contents of the “SleepyBiden.dat” file and converts it to bytes
binarySleepyBiden = bytes(open("SleepyBiden.dat").read(), encoding="utf-8")

# Generates a random one-time pad (OTP) key with the same length as the file content
key = generateOTPKey(binarySleepyBiden)

# Encrypts the contents of the SleepBiden.dat file using the OTP key
encryptedBinarySleepyBiden = otpEncrypt(binarySleepyBiden, key)

# Saves the encrypted text to a file called “Biden.dat” and stores the bytearray in a variable
savedBiden = open("Biden.dat","wb").write(encryptedBinarySleepyBiden)
encryptedBiden = encryptedBinarySleepyBiden

# Encrypts the OTP key using the Caesar Cipher with a shared key (4).
encryptedKey = encrypt(key)

# Sends the encrypted OTP key to Program B on the designated port (Socket Port 2500).
# Server name and ports for transmitting the key and data
serverName = "localhost"
keyPort = 2500
dataPort = 2501

# Creates a socket for transmitting the key
keySocket = socket(AF_INET, SOCK_STREAM)
keySocket.connect((serverName, keyPort))

# Sends the encrypted key to Program B using the designated key port (2500)
keySocket.send(bytes(encryptedKey,"utf-8"))
print("Program A has sent the encrypted OTP key.")

# Creates a socket for transmitting the data
dataSocket = socket(AF_INET, SOCK_STREAM)
dataSocket.connect((serverName, dataPort))

# Sends the encrypted "Biden.dat" file to Program B using the designated data port (2501)
dataSocket.send(encryptedBiden)
print("Program A has sent the encrypted file.")

# Closes the key socket
keySocket.close()
# Closes the data socket
dataSocket.close()
