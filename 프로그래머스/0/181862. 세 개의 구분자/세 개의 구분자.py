def solution(myStr):
    myStr = myStr.replace('a', ' ')
    myStr = myStr.replace('b', ' ')
    myStr = myStr.replace('c', ' ')
    answer = myStr.split()
    
    if len(answer) == 0 :
        answer = ["EMPTY"]
    
    return answer