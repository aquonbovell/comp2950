# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 06:48:37 2022

@author: neil_
"""
"""
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
import binascii


random_generator = Random.new().read
keyPair = RSA.generate(1024, random_generator)

pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))
msg = 'UWI is the greatest school ever!!!'
print('Original Message:', msg)
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg.encode())
print("Encrypted:", binascii.hexlify(encrypted))
decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted).decode()
print('Decrypted:', decrypted)
"""
"""
import rsa

# generate public and private keys with
# rsa.newkeys method,this method accepts
# key length as its parameter
# key length should be atleast 16
publicKey, privateKey = rsa.newkeys(512)

# this is the string that we will be encrypting
message = "UWI is the greatest school ever!!!\n"

# rsa.encrypt method is used to encrypt
# string with public key string should be
# encode to byte string before encryption
# with encode method
encMessage = rsa.encrypt(message.encode(),publicKey)

print("original string: ", message)
print("\nprivate key: ", privateKey)
print("\npublic key: ", publicKey)
print("\nencrypted string: ", encMessage)

# the encrypted message can be decrypted
# with rsa.decrypt method and private key
# decrypt method returns encoded byte string,
# use decode method to convert it to string
# public key cannot be used for decryption
decMessage = rsa.decrypt(encMessage, privateKey).decode()

print("\ndecrypted string: ", decMessage)
"""

"""
from Crypto.Cipher import DES

key = b'-8B key-'
cipher = DES.new(key, DES.MODE_OFB)
plaintext = b'sona si latine loqueris '
msg = cipher.iv + cipher.encrypt(plaintext)
print(msg)
"""
"""
from Crypto.Cipher import AES

key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_EAX)
data = b'Attack at dawn'

nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data)
print(ciphertext)

#decryption
key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_EAX, nonce)
plaintext = cipher.decrypt(ciphertext)
try:
     cipher.verify(tag)
     print("The message is authentic:", plaintext.decode())
except ValueError:
     print("Key incorrect or message corrupted")
"""
"""
import rsa

(pubkey, privkey) = rsa.newkeys(512)
message = 'Go left at the blue tree'.encode()
signature = rsa.sign(message, privkey, 'SHA-1')
message = 'Go left at the blue tree'.encode()
hash = rsa.compute_hash(message, 'SHA-1')
signature = rsa.sign_hash(hash, privkey, 'SHA-1')
message = 'Go left at the blue tree'.encode()
print(rsa.verify(message, signature, pubkey))
"""
