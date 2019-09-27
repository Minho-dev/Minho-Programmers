def solution(answers):
    answer = []
    a = [ 1, 2, 3, 4, 5 ] * ( len( answers ) // 5 + 1 )
    b = [ 2, 1, 2, 3, 2, 4, 2, 5 ] * ( len( answers ) // 8 + 1 )
    c = [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 ] * ( len( answers ) // 10 + 1 )
    a_count = 0
    b_count = 0
    c_count = 0
    
    for num in range( len( answers ) ):
        if answers[num] == a[num]:
            a_count += 1
        if answers[num] == b[num]:
            b_count += 1
        if answers[num] == c[num]:
            c_count += 1
        
    rank = [ [1, a_count], [2, b_count], [3, c_count] ]
    rank = sorted( rank, key = lambda key: key[1], reverse = True )
                    
    if rank[0][1] == rank[2][1]:
        answer = [rank[0][0], rank[1][0], rank[2][0]]
    elif rank[0][1] == rank[1][1]:
        answer = [ rank[0][0], rank[1][0] ]
    else:
        answer = [ rank[0][0] ]
        
    return answer
