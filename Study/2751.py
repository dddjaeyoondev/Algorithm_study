import sys

n = int(sys.stdin.readline())
upp = []
for i in range(n):
    upp.append(int(sys.stdin.readline()))
for i in sorted(upp):
    print(i)
