def solve():
    while True:
        num = input()
        re_num = num[::-1]

        if num == "0":
            exit()
        if num == re_num:
            print("yes")
        if num != re_num:
            print("no")


solve()
