def solution(s):
    answer = ''
    count = -1
    for a, b in enumerate( s ):
        if b != ' ':
            count += 1
            if count % 2 == 0:
                answer += b.upper()
            else:
                answer += b.lower()
        else:
            count = -1
            answer += b
    return answer
