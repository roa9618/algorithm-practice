def solution(arr):
    answer = []
    start_idx = -1
    end_idx = -1
    
    for i in range(len(arr)) :
        if arr[i] == 2 :
            if start_idx == -1 :
                start_idx = i
                end_idx = i
            else :
                end_idx = i
    
    if start_idx != -1 and end_idx != -1 :
        for i in range(start_idx, end_idx + 1) :
            answer.append(arr[i])
    else :
        answer = [-1]
    
    return answer