import socket

PORT = 8080
SOCK = socket.socket()

def createServer():
    print(f"Opening port: {PORT}")
    SOCK.bind(("127.0.0.1", PORT))
    SOCK.listen(1)
    
def sendResponce(connection, text):
    connection.sendall(bytearray("HTTP/1.1 200 ok\n", "ASCII"))
    connection.sendall(bytearray("\n", "ASCII"))
    connection.sendall(bytearray(
        "<html>\n"
        "<body>\n"
        "<h1>Your browser sent the following request:</h1>\n"
        f"<pre>{text}</pre>\n"
        "</body>\n"
        "</html>\n",
        "ascii"))
 
 
   
createServer()   
 
while True:
    print("wait for connection..")
    connection, addr = SOCK.accept()
    print(f"connected to {addr}")
    
    barr = connection.recv(1024)
    if barr:
        text = barr.decode("ascii").strip()
        sendResponce(connection, text)
    
    connection.close()

SOCK.close()