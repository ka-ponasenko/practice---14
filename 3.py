import re

stroka = input()
clear_stroka = re.sub(r'[^\w\s]', '', stroka)
list_stroka = clear_stroka.split()

print(list_stroka)
