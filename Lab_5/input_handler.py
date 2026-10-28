def giveInput(string):
    return input(string)

def askForMove(string):
    validEntries = ["R", "P", "S"]
    while True:
        move = giveInput(string).upper()
        if move in validEntries:
            return move
        else:
            print(f"{move} is not a valid move")