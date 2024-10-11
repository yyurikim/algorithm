from itertools import product

def solution(word):
    lst = list(word)
    alps = ['A', 'E', 'I', 'O', 'U']
    word_dict = []
    for i in range(1, 6):
        word_dict = word_dict + list(product(alps, repeat = i))
    
    word_dict = list(set(word_dict))
    
    words = []
    for lst in word_dict:
        words.append(''.join(lst))
    
    words.sort()
    
    
    for i in range(len(words)):
        if word == words[i]:
            answer = i+1
            break
            
            
    return answer