def solution(a, b):
    month = [ 'FRI', 'MON', 'TUE', 'FRI', 'SUN', 'WED', 'FRI', 'MON', 'THU', 'SAT', 'TUE', 'THU' ]
    week = [ 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT' ]
    idx = week.index( month[a-1] ) + ( b % 7 ) - 1
    answer = week[idx]
    return answer
