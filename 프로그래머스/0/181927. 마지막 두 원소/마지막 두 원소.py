def solution(num_list): 
    last_num = num_list[len(num_list) - 1]
    before_num = num_list[len(num_list) - 2]
    
    if last_num > before_num :
        num_list.append(last_num - before_num)
    else :
        num_list.append(last_num * 2)
    
    return num_list