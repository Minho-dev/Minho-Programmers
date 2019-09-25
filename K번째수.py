def solution(array, commands):
    answer = []
    
    for cmd in commands:
        ary = array[ cmd[0]-1 : cmd[1] ]
        ary = sorted( ary )
        answer.append( ary[cmd[2] - 1])
        
            
    return answer
