n = int(input())
stack = []
answer = []
flag = 0
cur = 1

for i in range(n):
    a = int(input())

    while cur <= a:
        stack.append(cur)
        answer.append("+")
        cur += 1

    if stack[-1] == a:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)
