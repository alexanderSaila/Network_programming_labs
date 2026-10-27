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
        print(people)

def printTopFive():
    minHeap = []
    size = 5
    
    for person, score in people.items():
        if len(minHeap) < 5:
            heapq.heappush(minHeap, (score, person))
        else:
            if score > minHeap[0][0]:
                heapq.heapreplace(minHeap, (score, person))
    
    print(minHeap)
        

loadDictionary()
printTopFive()