def encrypt(message="", key=4):
  secretMessage = ""
  for char in message:
    secretMessage += chr((ord(char) + key) % 127)
  return secretMessage

def decrypt(secretMessage="", key=4):
  message = ""
  for char in secretMessage:
    message += chr((ord(char) - key) % 127)
  return message