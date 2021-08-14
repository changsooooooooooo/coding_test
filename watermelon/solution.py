def solution(n):
    answer = ''
    for i in range(n):
        if i % 2:
            answer += '박'
            continue
        answer += '수'
    return answer
