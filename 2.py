numbers = list(map(int, input().split()))
amount = numbers.count(3)
if amount==1:
    numbers.remove(3)
    print(numbers)
else:
    print("Введите числа ещё раз")
