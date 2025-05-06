def solution(numbers, direction):
    ex = 0
    
    if direction == "right" :
        ex = numbers.pop(len(numbers) - 1)
        numbers.insert(0, ex)
    else :
        ex = numbers.pop(0)
        numbers.append(ex)
    
    return numbers