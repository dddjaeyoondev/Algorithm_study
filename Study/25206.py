A,B = [], [] 
N, M = map(int, input() .split())

for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row) 
for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)

for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end= " ")
    print()


A = []
for _ in range(3):
    sec = list(map(int,input().split()))
    A.append(sec)

for i in A:
    print(i)