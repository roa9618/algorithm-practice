def solution(age):
    dic = {}
    answer = ''
    
    for i in range(97, 107) :
        dic[i - 97] = chr(i)
    
    for i in str(age) :
        answer += dic.get(int(i))
    
    return answer