def solution(str1, str2):
    answer = 0
    
    if str2 not in str1 :
        answer = 2
    else :
        answer = 1
    
    return answer