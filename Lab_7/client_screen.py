import socket

PORT = 60003

sock = socket.socket()
ipAddress = input("Enter IP Address:")
sock.connect((ipAddress, PORT))
print("Connected")

while True:
    data = sock.recv(2048).decode("utf-8")
    print(data)