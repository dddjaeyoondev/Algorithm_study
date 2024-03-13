import sys

input = sys.stdin.readline

n = int(input())
gl = [int(input()) for i in range(n)]


print(sum(gl) // n)  # 산술평균
gl.sort()
print(gl[n // 2])  # 중앙값

gl = list(set(gl))  # 중복제거

zz = [0] * (max(gl) + 1)

for i in gl:
    zz[i] += 1

bzz = zz.index(max(zz))
print(gl[bzz])

print(max(gl) - min(gl))
