def solution(n):
    answer = ''
    while n // 3 != 0:
        re = n % 3
        n = n // 3
        
        if re == 1:
            answer += '1'
        elif re == 2:
            answer += '2'
        else:
            answer += '4'
            n = n - 1
    if n in [ 1, 2 ]:
        if n == 1:
            answer += '1'
        elif n == 2:
            answer += '2'

    return answer[::-1]
