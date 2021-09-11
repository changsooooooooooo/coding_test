import heapq
from collections import defaultdict

def solution(jobs):
    heapq.heapify(jobs)
    answer = []

    cur_time = 0

    temp = heapq.heappop(jobs)
    cur_time += temp[0]+temp[1]
    answer.append(temp[2])

    while True:
        candidate = list()
        check = False

        if not jobs:
            break

        while jobs:
            temp_2 = heapq.heappop(jobs)
            if temp_2[0]<=cur_time:
                if temp_2[2] == answer[-1]:
                    cur_time += temp_2[1]
                    check = True
                    continue
                candidate.append(temp_2)
                continue
            heapq.heappush(jobs, temp_2)
            break

        if not check and not candidate:
            temp = heapq.heappop(jobs)
            cur_time += temp[0]+temp[1]
            if answer[-1] != temp[2]:
                answer.append(temp[2])
            continue

        importance = defaultdict(int)
        if check:
            for c in candidate:
                heapq.heappush(jobs, c)
            continue

        if not check:
            for c in candidate:
                importance[str(c[2])] += c[-1]
        importance_list = []
        for key in importance:
            importance_list.append([importance[key], int(key)])
        importance_list.sort(key = lambda x : (-x[0], x[1]))
        cand = importance_list[0][1]
        answer.append(cand)
        for c in candidate:
            if c[2] == cand:
                cur_time+=c[1]
                continue
            heapq.heappush(jobs, c)

    return answer
