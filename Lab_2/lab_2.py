import heapq


people = dict()

def loadDictionary():

    with open("Lab_2/score2.txt") as file:
        for line in file:
            content = line.strip().split(" ")
            fullName = f"{content[2]} {content[3]}"

            if fullName not in people:
                people[fullName] = 0

            people[fullName] += int(content[4])



def printTopScore(amount):
    # store the top scorers in a min heap.
    minHeap = []
    
    for person, score in people.items():
        # while my heap size is not yet filled, just add the entry.
        if len(minHeap) < amount:
            heapq.heappush(minHeap, (score, person))
        else:
            # only replace entries if we encounter a higher score
            if score > minHeap[0][0]:
                heapq.heapreplace(minHeap, (score, person))
        
    # print out all the players in descending order
    for score, person in sorted(minHeap, reverse=True):
        print(f"{person}: {score}")
        

loadDictionary()
printTopScore(5)