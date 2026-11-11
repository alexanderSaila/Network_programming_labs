import socket

PORT = 60003

sock = socket.socket()
ipAddress = input("Enter IP Address:")
sock.connect((ipAddress, PORT))
print("Connected")

while True:
    userInput = input(":")

    if userInput.upper() == "Q":
        sock.shutdown(socket.SHUT_WR)
        sock.close()
        break
    else:
        barr = bytearray(userInput, "utf-8")
        sock.send(barr)