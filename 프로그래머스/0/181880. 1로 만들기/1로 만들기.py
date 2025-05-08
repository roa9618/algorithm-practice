def count(number) :
    count = 0
    
    while True :
        if number == 1 :
            break

        if number % 2 != 0 :
            number -= 1
        number //= 2
        count += 1
    
    return count

def solution(num_list):
    answer = 0
    
    for i in num_list :
        answer += count(i)
    
    return answer