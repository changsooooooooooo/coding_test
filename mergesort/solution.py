def conquer(left, right):
    answer = []
    i, j = 0, 0
    while i < len(left):
        while j < len(right):
            if right[j] < left[i]:
                answer.append(right[j])
                j += 1
                continue
            answer.append(left[i])
            i += 1
            break
        if j == len(right) and i < len(left):
            answer.extend(left[i:])
            break
        if j < len(right) and i == len(left):
            answer.extend(right[j:])
            break
    return answer


def divide(array):

    if len(array) == 1:
        return array

    start, end = 0, len(array)
    mid = (start+end)//2
    left = divide(array[start:mid])
    right = divide(array[mid:end])
    return conquer(left, right)


def solution(array, commands):
    answer = []
    for c in commands:
        temp_answer = divide(array[c[0]-1:c[1]])
        answer.append(temp_answer[c[2]-1])
    return answer

