def solution(n):
    answer = 0
    new = []
    for i in str(n):
        new.append(i)
    new = sorted( new, reverse = True )
    num = ''
    for i in new:
        num += i
    answer = int(num)
    return answer
