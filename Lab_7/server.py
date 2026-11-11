import socket
import select

PORT = 60003
sockL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockL.bind(("", PORT))
sockL.listen(1)

listOfSockets = [sockL]

print(f"Listening on port {PORT}")


def sendMessage(message):
    barr = bytearray(message, "utf-8")
    for sock in listOfSockets:
        if sock != sockL:
            sock.send(barr)


while True:
    tup = select.select(listOfSockets, [], [])
    sock = tup[0][0]

    if sock == sockL:
        connection, addr = sockL.accept()

        message = f"[{addr[0]}:{addr[1]}] (connected)"
        sendMessage(message)

        listOfSockets.append(connection)
    
    else:
        client = sock.getpeername()
        data = sock.recv(2048)
        
        if not data:
            listOfSockets.remove(sock)
            sock.close()
            
            message = f"[{client[0]}:{client[1]}] (disconnected)"
            sendMessage(message)
        else:
            message = f"[{client[0]}:{client[1]}] {data.decode("utf-8")}"
            sendMessage(message)

