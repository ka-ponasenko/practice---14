str1 = list(map(int, input().split()))
action = input()
side = action[0]
number = int(action[1:])

if side == 'L':
    number = number % len(str1)  
    str1 = str1[number:] + str1[:number]
    print(str1)
elif side == 'R':
    number = number % len(str1)
    str1 = str1[-number:] + str1[:-number]
    print(str1)
else:
    print("Введите корректную команду")