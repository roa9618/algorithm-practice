def solution(sides):
    max_side = max(sides)
    sides.pop(sides.index(max_side))
    
    if sum(sides) > max_side :
        return 1
    else :
        return 2