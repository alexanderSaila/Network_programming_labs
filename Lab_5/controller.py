from game_rules import GameRules
import input_handler

class Controller:

    def __init__(self, server, host = False):
        self._server = server
        self._server.establishConnection(host)

        self.setUpGame()

    def setUpGame(self):
        player = input_handler.giveInput("Enter your name: ")
        self._server.send(player)
        opponent = self._server.receive()
        self._game = GameRules(player, opponent)
    

    def playRound(self):
        playerMove = input_handler.askForMove(f"{self._game.getScoring()} | Make your move(R, P, S): ")
        self._server.send(playerMove)
        opponentMove = self._server.receive()

        return (self._game.getScoring(), self._game.playRound(playerMove, opponentMove))


