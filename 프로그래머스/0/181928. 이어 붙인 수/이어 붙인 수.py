def solution(num_list):
    answer1 = ''
    answer2 = ''
    
    for i in num_list :
        if int(i) % 2 != 0 :
            answer1 += str(i)
        else :
            answer2 += str(i)
    
    return int(answer1) + int(answer2)