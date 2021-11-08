def solution(s):
    answer = []
    i = 0
    while i < len(s):
        count = 1
        temp_idx = 0
        for j in range(i+1, len(s)):
            temp_idx = j
            if s[j] == s[i]:
                count += 1
                continue
            break
        answer.append(count)
        if s[i] == s[temp_idx] and temp_idx == len(s)-1:
            break
        if temp_idx == len(s)-1:
            answer.append(1)
            break
        i = temp_idx

    if s[0] == s[-1]:
        answer[0] += answer[-1]
        answer = answer[:-1]
    answer.sort()
    return answer

print(solution("wowwow"))
