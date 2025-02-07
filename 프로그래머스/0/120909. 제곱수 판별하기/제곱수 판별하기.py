import math

def solution(n):
    answer = 0
    sqrt = math.sqrt(n)
    
    if sqrt % 1 == 0 :
        answer = 1
    else :
        answer = 2
    
    return answer