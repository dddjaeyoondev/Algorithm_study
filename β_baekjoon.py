from collections import deque
import sys

N = int(sys.stdin.readline())

card = deque([i for i in range(1, N + 1)])

while len(card) > 1:
    card.popleft()
    num = card.popleft()
    card.append(num)

print(card[0])
