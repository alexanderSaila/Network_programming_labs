from server_handler import ServerHandler
from controller import Controller
 
myPort = 60003

def gameLoop():
    while True:
        round = controller.playRound()
        print(round[1])
        playerScore = round[0][0]
        opponentScore = round[0][1]
        if playerScore > 9:
            result = "YOU WON!!"
            break
        elif opponentScore > 9:
            result = "YOU LOST :("
            break
    gameEnd(result)


def gameEnd(result):
    print(f"{result}\n Your score:{playerScore} vs your opponents score:{opponentScore}")


while True:
    ans = input("Do you want to be Server(S) or Clien(C): ").upper()
    serverHandler = ServerHandler(myPort)

    match ans:
        case "S":
            controller = Controller(serverHandler, True)
            gameLoop()
            break
        case "C":
            controller = Controller(serverHandler)
            gameLoop()
            break
        case _:
            print("Try again")