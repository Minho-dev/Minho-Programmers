def solution(arr, divisor):
    answer = []
    answer = sorted([k for k in arr if k % divisor == 0])
    if len(answer) == 0:
        answer.append(-1)
    return answer
