num = int(input())

nums_house = 1
count = 1

while num > nums_house:
    nums_house += 6 * count
    count += 1
print(count)
