def fibonacci(n):
    previousNum = 0
    nextNum = 1
    while previousNum < n:
        yield previousNum
        previousNum, nextNum = nextNum, previousNum+nextNum


for i in fibonacci(1000000):
    print(i)