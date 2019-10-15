def solution(n):
    answer = 0
    import math
    sol = math.sqrt(n)
    if sol % 1 == 0:
        answer = (int(sol) +1 ) ** 2
    else:
        answer = -1
    return answer
