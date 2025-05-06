def solution(myString):
    answer = myString.split('x')
    
    for i in range(answer.count("")) :
        answer.remove("")
    
    answer.sort()
    
    return answer