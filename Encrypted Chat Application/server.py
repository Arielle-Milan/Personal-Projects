import socket
from encrypt import decrypt, encrypt

#set up the server socket
server = socket.socket()
server.bind(('localhost', 9999))
server.listen(1)
print("Server listening...")

#accept one client connection
conn, addr = server.accept()
print("Connected:", addr)

#continuous chat loop
while True:
    msg = conn.recv(1024)  # Receive encrypted message
    if msg:
        print("Client:", decrypt(msg))  # Decrypt and print
        reply = input("You: ")  # Get your response
        conn.send(encrypt(reply))  # Encrypt and send back
