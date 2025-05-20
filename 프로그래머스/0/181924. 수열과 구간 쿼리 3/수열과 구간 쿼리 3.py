def solution(arr, queries):   
    for i in queries :
        ex = arr[i[0]]
        arr[i[0]] = arr[i[1]]
        arr[i[1]] = ex
    
    return arr