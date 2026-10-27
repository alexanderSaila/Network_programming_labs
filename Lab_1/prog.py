import random

def getLotto():
    mySet = set()
    while len(mySet) < 7:
        mySet.add(random.randint(1,35))

    return mySet