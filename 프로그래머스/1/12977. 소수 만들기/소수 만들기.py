import math

def is_prime(num) :
    if num < 2 :
        return False
    elif num == 2 :
        return True
    else :  
        for i in range(2, int(math.sqrt(num)) + 1) :
            if num % i == 0 :
                return False
    
    return True

def solution(nums):
    answer = 0
    num_list = []

    for i in range(len(nums)) :
        for j in range(i + 1, len(nums)) :
            for k in range(j + 1, len(nums)) :
                num_list.append(nums[i] + nums[j] + nums[k])
                
    for i in num_list :
        if is_prime(i) :
            answer += 1
        else :
            continue
                
    return answer