import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

queue = deque()

for i in range(n):
    num = input().split()

    if num[0] == "1":
        queue.append(int(num[1]))

    if num[0] == "2":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue) - 1])
            queue.pop()
    if num[0] == "3":
        print(len(queue))

    if num[0] == "4":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    if num[0] == "5":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue) - 1])
