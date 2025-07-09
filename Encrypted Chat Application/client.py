import socket
from encrypt import decrypt, encrypt

#connect to the server
client = socket.socket()
client.connect(('localhost', 9999))

#continuous chat loop
while True:
    msg = input("You: ")  # Get user input
    client.send(encrypt(msg))  # Encrypt and send
    reply = client.recv(1024)  # Receive and decrypt reply
    print("Server:", decrypt(reply))
