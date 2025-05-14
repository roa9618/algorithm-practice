def solution(my_string):
    upper = []
    lower = []
    
    for i in range(26) :
        upper.append(0)
        lower.append(0)
    
    for i in my_string :
        if i.isupper() :
            upper[ord(i) - 65] += 1
        elif i.islower() :
            lower[ord(i) - 97] += 1
    
    answer = upper + lower
    
    return answer