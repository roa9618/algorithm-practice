def solution(num_list, n):
    answer = []
    
    for i in range(len(num_list) // n) :
        ex = []
        
        for j in range(n) :
            ex.append(num_list.pop(0))
            
        answer.append(ex)
    
    return answer