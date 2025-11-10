numbers = list(map(int, input().split()))

new_list = []

for i in range(1, 9):
    new_list.append(numbers[i-1] + numbers[i+1])

print(new_list)



