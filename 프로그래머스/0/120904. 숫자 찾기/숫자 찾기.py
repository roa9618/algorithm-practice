def solution(num, k):
    arr = []
    answer = -1
    
    for i in str(num) :
        arr.append(int(i))
    
    if k in arr :
        answer = arr.index(k) + 1
    
    return answer