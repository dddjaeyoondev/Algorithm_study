# deque 생성, 요세푸스 순열 생성
# k - 1 번째 노드까지 deq 맨 뒤로 이동
# k번째 노드 삭제 후 결과 배열에 추가

import sys
from collections import deque

n, k = map(int, input().split())

deq = deque([i for i in range(1, n + 1)])  # deq 리스트 생성

res = []

while len(deq) != 0:  # deq의 길이가 0이 아닐때까지
    for _ in range(k - 1):  # k 입력받은 만큼
        deq.append(deq.popleft())  # deq의 맨 앞에서 pop 한 값을 deq 에 append
    res.append(str(deq.popleft()))  # deq 의 맨앞. pop 값 str변환. res 에 append


print("<" + ", ".join(res) + ">")  # join 함수 -> 리스트를 문자열로
