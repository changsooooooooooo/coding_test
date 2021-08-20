def solution(s):
    answer_s = ''
    char_part = ''

    candidate = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i, c in enumerate(s):
        if c.isnumeric():
            answer_s += c
            continue
        char_part += c
        for j in range(10):
            if candidate[j] == char_part:
                answer_s += str(j)
                char_part = ""
                break

    return int(answer_s)
