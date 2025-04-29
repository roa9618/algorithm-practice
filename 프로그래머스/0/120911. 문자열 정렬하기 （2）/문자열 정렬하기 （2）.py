def solution(my_string):
    array = []
    result = ""
    
    for i in my_string :
        array.append(i.lower())
    
    array.sort()
    
    for i in array :
        result += i
    
    return result