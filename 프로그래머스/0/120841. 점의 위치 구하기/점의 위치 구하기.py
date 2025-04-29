def solution(dot):
    result = -1
    
    if dot[0] < 0 and dot[1] < 0 :
        result = 3
    elif dot[0] < 0 and dot[1] > 0 :
        result = 2
    elif dot[0] > 0 and dot[1] < 0 :
        result = 4
    else :
        result = 1
        
    return result