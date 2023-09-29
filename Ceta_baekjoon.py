n = int(input())
stack = []
answer = []
stack_count = 1
flag = 0


for i in range(n):
    a = int(input())

    while stack_count <= a:
        stack.append(stack_count)
        answer.append("+")
        stack_count += 1

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
