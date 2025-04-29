from math import sqrt

def solution(n):
    answer = []
    
    for i in range(1, int(sqrt(n)) + 1) :
        if n % i == 0 :
            answer.append(i)
            answer.append(n // i)
    
    answer = list(set(answer))
    answer.sort()
    
    return answer