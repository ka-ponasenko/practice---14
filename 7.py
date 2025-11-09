number_list = list(map(int, input().split()))
chet = []
nechet = []
for i in number_list:
    if i%2==0:
        chet.append(i)
    else:
        nechet.append(i)

sum_chet = sum(i for i in chet)
sum_nechet = sum(i for i in nechet)

print(sum_chet, sum_nechet)