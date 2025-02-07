def solution(numbers):
    answer = -10000 * 10000
    
    for i in range(len(numbers)) :
        for j in range(i + 1, len(numbers)) :
            mul = numbers[i] * numbers[j]
            
            if answer < mul :
                answer = mul
    
    return answer