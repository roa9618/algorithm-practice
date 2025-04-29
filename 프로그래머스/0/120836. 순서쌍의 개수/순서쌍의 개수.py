import math

def solution(n):
    result = 0
    
    for i in range(1, int(math.gcd(n, n))) :
        if n % i == 0 :
            result += 1

    return result + 1