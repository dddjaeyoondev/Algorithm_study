num = int(input())
array = [[0] * 100 for _ in range(100)] # 100 * 100 
for _ in range(num):
    y1, x1 = map(int,input().split())

    for i in range(x1, x1+10):
        for j in range(y1, y1+10):
            array[i][j] = 1 

result = 0 
for k in range(100):
    result += array[k].count(1) 


print(result)


    
#     2563에 대해 설명을 해드리겠습니다. 

# 우선 색종이라고 해서 테두리를 자르거나, 진짜 종이 처럼 취급해서 할 필요는 없습니다. 
# 우리에겐 ‘2차원 배열’ 이라는 힌트가 있죠. 

# 문제를 봅시다. 

# 문제를 보시면, 모든 검은색 영역의 넓이를 구하는 것입니다. 
# 자 우리는 이걸 어떻게 해야 할까요? 

# 바로 이것을 배열로 표현을 하는 것이죠. 기하를 써야 하나요? 아닙니다. 

# 힌트를 하나 드리자면, 우리는 0으로 된 빈 숫자열을 만들 것입니다. 

# 숫자열이라고 하니깐 감이 오시나요? 그리고 우리는 색종이의 넓이를, 즉, 
# 주어진 가로 길이와 세로 길이의 좌표만큼, 0들을 1로 바꿀 것입니다. 

# 그리고 마지막에 1의 갯수만큼이 넓이가 되는것이지요. 무슨 말인지 알겠습니까? 

# 이로써 따로 겹쳐져있는 색종이의 넓이만큼 빼거나, 할 필요가 없습니다. 

# 문제에서 주어진 최대 넓이인 100 * 100 짜리 빈 이차원 배열을 만들어 준다음, 

# 그 안에서 num 만큼 반복하는 것이죠. 

# 참고로, 넓이는 10으로 통일되었습니다. 

# 자 그렇다 함은, 여기서 3 하고 7을 입력 받았을 때, 

# 반복문을, 3 에서 3 + 10  까지, 
# 7 에서 7 + 10 까지, 왼쪽 아래 모서리의 좌표로부터 가로새로, 행 열, row, column을 각각 10 씩 퍼지게 만들어서 10 * 10 짜리 1로 이루어진 색종이를 만들어 내게 되는 것입니다. 어떄요. 재밌죠? 

# 이렇게해서 마지막에, 100만큼 돌려서, 1이 얼마만큼 있나, count() 함수를 사용해서 계산하면 나오게 되는 것입니다. ! 
