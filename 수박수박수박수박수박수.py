def solution(n):
    s = '수박'
    return s * (n//2) + s[0]*(n%2)
