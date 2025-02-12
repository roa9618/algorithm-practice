def solution(num_list):
    mul_value = 1
    sum_value = sum(num_list) ** 2
    
    for i in num_list :
        mul_value *= i
        
    if sum_value > mul_value :
        return 1
    elif sum_value < mul_value :
        return 0