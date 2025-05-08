def solution(my_string, s, e):    
    ex = my_string[s : e + 1]
    ex = ex[::-1]
    answer = my_string[0 : s] + ex + my_string[e + 1 :]
    
    return answer