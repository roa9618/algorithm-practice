from math import sqrt

def solution(k, d):    
    count = 0
    answer = 0
    
    for x in range(0, d + 1, k) :
        count = sqrt(d ** 2 - x ** 2) // k + 1
        answer += count
    
    return answer