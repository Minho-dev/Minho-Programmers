def solution(a, b):
    answer = 0
    
    return sum(range(a,b+1)) if a <= b else sum(range(b,a+1))
