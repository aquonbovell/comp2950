from socket import *
from Part1 import decrypt

# Modified decrypt function to handle OTP Decryption
def otpDecrypt(ciphertext, key=4):
    decryptedData = bytearray()
    for i in range(len(ciphertext)):                                       
        decryptedData.append(ciphertext[i] ^ int(key[i]))
    return decryptedData.decode("utf-8")

# Server name and ports for transmitting the key and data
serverName = "localhost"
keyPort = 2500
dataPort = 2501

# Creates a socket for receiving the key
keySocket = socket(AF_INET, SOCK_STREAM)
keySocket.bind((serverName, keyPort))
keySocket.listen(1)
print("Program B is ready to receive the encrypted OTP key...")

# Accepts the connection from Program A and receives the encrypted OTP key
keyConn, keyAddr = keySocket.accept()
encryptedKey = keyConn.recv(4096).decode("utf-8")
print("Program B has received the encrypted OTP key...")
keyConn.close()

# Creates a socket for receiving the data
dataSocket = socket(AF_INET, SOCK_STREAM)
dataSocket.bind((serverName, dataPort))
dataSocket.listen(1)
print("Program B is ready to receive the encrypted file...")

# Accepts the connection from Program A and receives the encrypted file
dataConn, dataAddr = dataSocket.accept()
encryptedData = dataConn.recv(4096)
dataConn.close()

# Saves the encrypted file to the hard drive
with open("Biden.dat", "wb") as savedFile:
    savedFile.write(encryptedData)

# Opens the newlysaved Biden.dat file
with open("Biden.dat", "rb") as readSavedFile:
    encyrptedBiden = readSavedFile.read()

# Decrypts the OTP key using the shared key (k) and the Caesar Cipher
key = decrypt(encryptedKey)
print("Decrypted OTP key...")

# Decrypts the message in “Biden.dat” using the OTP key
decryptedBiden = otpDecrypt(encyrptedBiden, key)
print("Decrypted Biden.dat contents using decrypted OTP key...")

# Prints the decrypted contents of “Biden.dat” to the screen
print(f"\nDecrypted File Content: \n{decryptedBiden}")