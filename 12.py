def count_holes_letters(text):
    hole_letters = {'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'}
    
    with_holes = 0
    without_holes = 0
    
    for char in text:
        if char.isalpha(): 
            if char in hole_letters:
                with_holes += 1
            else:
                without_holes += 1
    
    return with_holes, without_holes

def multiple_holes(text):
    hole_letters = {'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'}
    
    words = text.split()
    result_words = []
    
    for word in words:
        hole_count = sum(1 for char in word if char in hole_letters)
        
        if hole_count >= 2:
            result_words.append(word)
    
    return result_words

text = input()

holes, no_holes = count_holes_letters(text)
print(holes, no_holes)

words_with_holes = multiple_holes(text)
print(words_with_holes)