import re

words = []
while True:
    line = input().strip()
    if line == "":
        break
    
    clean_line = re.sub(r'[^\w\s]', '', line)
    line_words = clean_line.lower().split()
    words.extend(line_words)

unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)

sorted_words = sorted(unique_words, key=lambda word: (-words.count(word), words.index(word)))

for word in sorted_words:
    print(word)
