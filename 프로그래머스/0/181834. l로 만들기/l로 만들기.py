def solution(myString):
    answer = ''
    
    for i in myString :
        if ord(i) > ord('l') :
            answer += i
        else :
            answer += 'l'
    
    return answer