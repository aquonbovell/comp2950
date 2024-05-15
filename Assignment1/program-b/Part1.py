# Part 1 - Extended Caesar's Cipher
def encrypt(message, key=4):                                                # Function for encoding a given message.
    ciphertext = ""
    for i in message:                                                       # Loops through all the elements of the message and concatanates it to a string, after 
        ciphertext += chr((ord(i) + key) % 127)                             # applying the formula (k + ek) % 127 to every element in the list, uses the ord() function to  get the ascii code for the characters.
    return ciphertext                                                       # returns the encrypted message


def decrypt(ciphertext, key=4):                                             # does the same as encrypt(), however uses the formula (k - dk) % 127 to decrypt the encrypted message
    message = ""
    for i in ciphertext:                                                    # Loops through all the elements of the message and concatanates it to a string, after 
        message += chr((ord(i) - key) % 127)                                # applying the formula (k + ek) % 127 to every element in the list, uses the ord() function to get the ascii code for the characters.
    return message                                                          # returns the decrypted message


if __name__ == "__main__":
    message = input("Enter a message: ")                                    # Prompts user to enter a message to encrypt.
    eKey = int(input("Enter your encryption key: "))                        # Prompts user to enter their key to encrypt the message.
    dKey = int(input("Enter your decryption key: "))                        # Prompts user to enter their key to decrypt the message.
    print(f"Encryptd Message: {encrypt(message, eKey)}")                    # prints the encryptd message
    print(f"Decryptd Message: {decrypt(encrypt(message, eKey),dKey)}")      # prints the decryptd message           