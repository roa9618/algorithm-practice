def solution(s):
    answer = ''
    
    for i in s :
        if s.count(i) == 1 :
            answer += i
    
    arr = sorted(answer)
    answer = ''
    
    for i in arr :
        answer += i
    
    return answer