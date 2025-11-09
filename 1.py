n = 0
numbers = []
new_list = []
while n < 10:
    numbers.append(int(input()))
    n += 1

for i in range(len(numbers)-2):
    new_list.append(numbers[i] + numbers[i+1] + numbers[i+2])

print(new_list)
    


