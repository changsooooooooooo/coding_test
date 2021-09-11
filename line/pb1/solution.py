def solution(student, k):
    answer = 0

    index = [i for i in range(len(student)) if student[i] == 1]
    if len(index) < k:
        return 0

    if k == 1:
        return (index[0]+1)*(len(student)-index[0])

    for idx in range(len(index)-k+1):
        if idx == 0:
            next_idx = index[idx+k-1]
            if len(index)<=idx+k:
                limit_idx = len(student)
            else:
                limit_idx = index[idx+k]
            before = index[idx]
            after = limit_idx-next_idx
            if after == 1:
                answer+=before+1
                continue
            answer += before*after
            continue

        next_idx = index[idx+k-1]
        if len(index)<=idx+k:
            limit_idx = len(student)
        else:
            limit_idx = index[idx+k]
        before = index[idx]-index[idx-1]
        after = limit_idx-next_idx
        answer += before*after

    return answer
