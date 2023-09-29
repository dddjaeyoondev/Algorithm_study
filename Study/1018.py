N = 8
str1 = "WBWBWBWB"
str2 = "BWBWBWBW"
pivot1 = [str1, str2, str1, str2, str1, str2, str1, str2]
pivot2 = [str2, str1, str2, str1, str2, str1, str2, str1]


def solve():
    a, b = [int(x) for x in input().split()]  # 입력
    arr = []
    for i in range(a):
        arr.append(input())  # 입력
    rst = float("inf")  # 제일 작은 값을 구하기 위해 제일 큰 값 지정. 부동 소수점.
    for i in range(a - N + 1):  # 그냥 a-7헤도 됨.
        for j in range(b - N + 1):
            count = 0  # 0부터 시작해서 다른게 몇번인지 count
            for p in range(N):
                for q in range(N):
                    if arr[i + p][j + q] == pivot1[p][q]:
                        count += 1
            rst = min(rst, count)
            count = 0  # 0부터 시작해서 다른게 몇번인지 count
            for p in range(N):
                for q in range(N):
                    if arr[i + p][j + q] != pivot2[p][q]:
                        count += 1
            rst = min(rst, count)
    print(rst)


solve()

# -------------------------------------------------------------------------

# N = 8
# str1 = "WBWBWBWB"
# str2 = "BWBWBWBW"
# pivot1 = [str1, str2, str1, str2, str1, str2, str1, str2]
# pivot2 = [str2, str1, str2, str1, str2, str1, str2, str1]


# def solve():
#     a, b = map(int, input().split())
#     arr = []

#     for i in range(a):
#         arr.append(input())

#     rst = float("inf")  # infinite

#     for i in range(a - N + 1):
#         for j in range(b - N + 1):
#             count = 0
#             for p in range(N):
#                 for q in range(N):
#                     if arr[p + i][q + j] != pivot1[p][q]:
#                         count += 1
#             rst = min(rst, count)

#             count = 0
#             for p in range(N):
#                 for q in range(N):
#                     if arr[p + i][q + j] != pivot2[p][q]:
#                         count += 1

#             rst = min(rst, count)
#     print(rst)


# solve()

# ---------------------------------------------------------------------

# n, m = map(int, input().split())
# board = []
# result = []

# for _ in range(n):
#     board.append(input())

# for i in range(n - 7):
#     for j in range(m - 7):
#         draw1 = 0
#         draw2 = 0

#         for a in range(i, i + 8):
#             for b in range(j, j + 8):
#                 if (a + b) % 2 == 0:
#                     if board[a][b] != "B":
#                         draw1 += 1
#                     if board[a][b] != "W":
#                         draw2 += 1
#                 else:
#                     if board[a][b] != "W":
#                         draw1 += 1
#                     if board[a][b] != "B":
#                         draw2 += 1

#         result.append(draw1)
#         result.append(draw2)

# print(min(result))
