def solution(a, d, included):
    ex = 0
    answer = 0
    
    for i in range(len(included)) :
        if i == 0 :
            ex += a
        else :
            ex += d
        
        if included[i] == True :
            answer += ex
    
    return answer