def solution(intStrs, k, s, l):
    answer = []
    
    for i in range(len(intStrs)) :
        ex = int(intStrs[i][s : s + l])
        if ex > k :
            answer.append(ex)
    
    return answer