from collections import defaultdict


def solution(gems):
    gemTypeTotal = len(set(gems))
    gemLength = len(gems)
    start = 0
    end = 0
    answer = []
    current_gems = defaultdict(int)
    current_gems[gems[0]] += 1

    while start < gemLength or end < gemLength:
        if len(current_gems) < gemTypeTotal:
            end += 1
            if end == gemLength:
                break
            current_gems[gems[end]] += 1
        else:
            answer.append(([start+1, end+1], end-start))
            current_gems[gems[start]] -= 1
            if current_gems[gems[start]] == 0:
                del current_gems[gems[start]]
            start += 1

    answer = sorted(answer, key=lambda x: (x[1], x[0]))
    return answer[0][0]
