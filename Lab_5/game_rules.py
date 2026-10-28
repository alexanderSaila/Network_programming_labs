class GameRules:

    _moves = {
        "R": {"name": "Rock", "beats": "S"},
        "P": {"name": "Paper", "beats": "R"},
        "S": {"name": "Scissor", "beats": "P"}
    }

    def __init__(self, player, opponent):
        self._player = player
        self._opponent = opponent
        self._players = {self._player: 0, self._opponent: 0}
        print(f"Game starting between {self._player} and {self._opponent}")


    def playRound(self, playerMove, opponentMove):
        player = {"name": self._player, "move": self._moves[playerMove]["name"]}
        opponent = {"name": self._opponent, "move": self._moves[opponentMove]["name"]}

        if playerMove == opponentMove:
            return f"Both played {player["move"]} Its a tie!"
        elif self.isPlayerWinner(playerMove, opponentMove):
            self._players[self._player] += 1
            return self.winnerOfRound(player, opponent)
        else:
            self._players[self._opponent] += 1
            return self.winnerOfRound(opponent, player)


    def winnerOfRound(self, winner, loser):
        return  f"{winner["name"]} played {winner["move"]} and won over {loser["name"]}'s {loser["move"]}"


    def isPlayerWinner(self, playerMove, opponentMove):
        return self._moves[playerMove]["beats"] == opponentMove


    def getScoring(self):
        return (self._players[self._player], self._players[self._opponent])