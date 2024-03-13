n = int(input())

for _ in range(n):
    ps = input()
    stack = []

    for i in ps:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                stack.append(i)
                break
            else:
                stack.pop()
    if len(stack) != 0:
        print("NO")
    else:
        print("YES")


#   놓친점 1: 그냥 break 해버리면, len(stack) == 0 이 된채로 나와서 YES 를 출력하게 됨.
#           그리하여 append 를 해준것임.
