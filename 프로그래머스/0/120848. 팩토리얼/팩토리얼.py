def factorial(n) :
    sum = 1
    
    for i in range(n, 1, -1) :
        sum *= i
    
    return sum

def solution(n):
    answer = 0 
    
    for i in range(1, 12) :
        if factorial(i) > n :
            answer = i - 1
            break
    
    return answer