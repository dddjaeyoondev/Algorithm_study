num_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'                          
n,b = input().split() 
answer = 0 

for i , num in enumerate(n[::-1]):
    answer += int(b) ** i * num_list.index(num)
print(answer)


# 2745 진법변환 
# 0부터 Z까지 문자열 
# 그냥 0부터 9 까지 해놓고 그 이상은 표현하기에 어려움. 
# 그래서 알파벳은 그냥 