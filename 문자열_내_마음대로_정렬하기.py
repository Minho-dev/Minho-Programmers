def solution(strings, n):
    answer = []
    dic = {}
    for i in strings:
        dic[i[n]] = []
    for j in strings:
        dic[j[n]].append(j)
    keys = sorted( list( dic.keys() ) )
    for key in keys:
        key = sorted( dic[key] )
        for k in key:
            answer.append(k)
    return answer
