def solution(size):
    answer = 0
    start, end = 0, 0

    if int(size/3) == size/3:
        start = int(size/3)
    else:
        start = int(size/3)+1
    if int(size/2) == size/2:
        end = int(size/2)
    else:
        end = int(size/2)+1

    for i in range(start, end):
        answer += int(3*i/2 - size/2 +1)

    return answer
