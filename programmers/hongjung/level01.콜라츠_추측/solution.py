def solution(num):
    repeat = 0
    
    while num != 1:
        if repeat == 500:
            return -1
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        repeat += 1
        
    return repeat
