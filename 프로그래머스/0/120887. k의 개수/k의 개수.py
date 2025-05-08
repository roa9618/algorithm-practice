def solution(i, j, k):
    count = 0
    
    for i in range(i, j + 1) :
        for j in str(i) :
            if str(k) in j :
                count += 1
    
    return count