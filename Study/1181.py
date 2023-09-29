def solve():
    num = int(input())

    words = [input() for i in range(num)]

    words = list(set(words))  # 중복처리
    words.sort()  # 정렬 (alphabet)
    words.sort(key=len)  # 정렬(length)

    for i in words:
        print(i)


solve()
