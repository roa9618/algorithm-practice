def solution(before, after):
    answer = 0
    before_arr = []
    after_arr = []
    
    for i in range(len(before)) :
        before_arr.append(before[i])
        after_arr.append(after[i])
        
    before_arr.sort()
    after_arr.sort()
    
    if before_arr == after_arr :
        answer = 1
    
    return answer