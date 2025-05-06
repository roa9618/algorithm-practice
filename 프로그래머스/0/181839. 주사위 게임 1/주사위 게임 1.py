def solution(a, b):
    count = 0
    
    if a % 2 != 0 :
        count += 1
    
    if b % 2 != 0 :
        count += 1
    
    if count == 2 :
        answer = a ** 2 + b ** 2
    elif count == 1 :
        answer = 2 * (a + b)
    else :
        answer = abs(a - b)
    
    return answer