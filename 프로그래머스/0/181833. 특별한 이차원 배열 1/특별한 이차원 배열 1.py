def solution(n):
    answer = []
    
    for i in range(n) :
        ex = []
        
        for j in range(n) :
            if i == j :
                ex.append(1)
            else :
                ex.append(0)
        
        answer.append(ex)
    
    return answer