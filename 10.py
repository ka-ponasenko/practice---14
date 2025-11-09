lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
start = int(input())  
end = int(input())    
start_index = start - 1
end_index = end - 1

elements_to_transfer = lst1[start_index:end_index+1]

reversed_elements = elements_to_transfer[::-1]

lst2.extend(reversed_elements)

del lst1[start_index:end_index+1]

print(lst1)
print(lst2)
