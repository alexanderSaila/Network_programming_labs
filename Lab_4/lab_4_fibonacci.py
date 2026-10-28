def fibonacci(n):
    previousNum = 0
    nextNum = 1
    while previousNum < n:
        yield previousNum
        previousNum, nextNum = nextNum, previousNum+nextNum

count = 1000000
a = fibonacci(count)

for i in range(count):
    print(a.__next__())