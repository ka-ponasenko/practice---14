import re

stroka = input()
clear_stroka = re.sub(r'[^\w\s]', '', stroka)
words = clear_stroka.split()

unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)

print(unique_words)
