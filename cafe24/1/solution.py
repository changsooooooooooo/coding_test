def solution(n):
    answer = 0
    count = 0

    for i in range(1, n+1):
        count += i*2-1

    for i in range(count, count-3, -1):
        answer += i*2-1

    return answer
