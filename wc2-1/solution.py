from collections import defaultdict


def solution(scores):
    answer = ''

    scores2 = [[scores[i][j] for i in range(len(scores))] for j in range(len(scores))]

    for i, s in enumerate(scores2):
        self_score = s[i]
        s.sort()
        dictionary = defaultdict(int)
        max_, min_ = s[-1], s[0]
        for idx in range(len(s)):
            dictionary[s[idx]] += 1
        count, sum = 0, 0

        if self_score == min_ or self_score == max_:
            if dictionary[self_score] == 1:
                dictionary[self_score] = 0

        for key in dictionary:
            count += dictionary[key]
            sum += dictionary[key]*key

        if count == 0:
            answer += "F"
            continue

        if 90 <= sum/count:
            answer += "A"
            continue
        if 80 <= sum/count < 90:
            answer += "B"
            continue
        if 70 <= sum/count < 80:
            answer += "C"
            continue
        if 50 <= sum/count < 70:
            answer += "D"
            continue
        answer += "F"

    return answer
