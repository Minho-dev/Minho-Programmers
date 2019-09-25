def solution(s):

    x = len( s )
    if x % 2 == 0:
        a = x // 2
        answer = s[ a-1 : a+1 ]
    else:
        a = x // 2
        answer = s[ a ]
    return answer
