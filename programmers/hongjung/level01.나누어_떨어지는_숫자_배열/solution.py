def solution(nums, divisor):
    answer = []
    
    for num in nums:
        if num % divisor == 0:
            answer.append(num)
            
    return [-1] if len(answer) == 0 else sorted(answer)
