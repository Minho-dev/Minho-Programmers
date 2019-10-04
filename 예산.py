def solution(d, budget):
    answer = 0
    
    for money in sorted( d ):
        if budget < money:
            break
        else:
            budget -= money
            answer += 1
    return answer
