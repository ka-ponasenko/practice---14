text = input()

def tolist(string1):
    list_elem = []
    for char in string1:
        list_elem.append(char)
    list_elem.sort()
    new_string = "".join(list_elem)
    return new_string

print(tolist(text))