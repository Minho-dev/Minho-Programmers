def solution(s, n):
    answer = ''
    upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2
    low = upp.lower()
    for i in s:
        if i in upp:
            idx = upp.find(i)
            answer += upp[idx + n ]
        elif i in low:
            idx = low.find(i)
            answer += low[idx + n ]
        else:
            answer += ' '
    return answer
