import socket

class ServerHandler:

    def __init__(self, port):
        self._port = port
    

    def establishConnection(self, host = False):
        self._host = host
        if(host):
            self._connection = self.createServer()
        else:
            self._connection = self.findServer()


    def createServer(self):
        print(f"Opening port: {self._port}")
        sock = socket.socket()
        sock.bind(("", self._port))
        
        sock.listen(1)
        print("wait for other player..")
        connection, addr = sock.accept()
        print(f"connected to {addr}")

        return connection


    def findServer(self):
        serverIp = input("Enter IP-address: ")
        sock = socket.socket()
        sock.connect((serverIp, self._port))
        print("Sucessfully connected")

        return sock
    

    def send(self, string):
        barr = bytearray(string, "utf-8")
        self._connection.send(barr)
    

    def receive(self):
        barr = self._connection.recv(1024)
        return barr.decode("utf-8").strip()


    def close(self):
        self._connection.close()