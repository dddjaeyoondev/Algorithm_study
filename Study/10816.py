import sys

N = int(sys.stdin.readline())
N_li = sorted(
    [*map(int, sys.stdin.readline().split())]
)  # 입력받고, 결과를 리스트로 저장. 그다음 sorted
M = int(sys.stdin.readline())
M_li = [*map(int, sys.stdin.readline().split())]  # 입력받고, 결과를 리스트로 저장.

count = {}  # dictionary 로 저장.


for i in N_li:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in M_li:
    if i in count:
        print(count[i], end=" ")
    else:
        print(0, end=" ")

# dict 와 key 를 이용해서 푼 문제
