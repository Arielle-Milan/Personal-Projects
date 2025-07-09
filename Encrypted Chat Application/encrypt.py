from Crypto.Cipher import AES
import base64

#16-byte secret key 
key = b'ThisIsA16ByteKey'

#pad the message 
#it must be a multiple of 16 bytes
def pad(text):
    return text + b' ' * (16 - len(text) % 16)

#encrypt the message
def encrypt(message):
    cipher = AES.new(key, AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(pad(message.encode())))

#decrypt the message
def decrypt(encrypted):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(base64.b64decode(encrypted)).strip().decode()
