__author__ = 'hira'
import socket

host = "localhost"
port = 10500

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, port))

while True:
    print("waiting...")
    print(client.recv(4096))
