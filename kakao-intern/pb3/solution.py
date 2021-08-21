from collections import deque


def solution(n, k, cmd):
    answer = ''
    exist_list = [True for _ in range(n)]
    current_table = [i for i in range(n)]
    cache = deque()
    r_cus = k

    for c in cmd:
        print("pos : ", r_cus)
        print("cache : ", cache)
        print("cmd : ", c)
        print("current_table : ", current_table)
        if c[0] == "D":
            r_cus += int(c[2])
            continue
        if c[0] == "U":
            r_cus -= int(c[2])
            continue
        if c == "C":
            exist_list[current_table[r_cus]] = False
            cache.append(current_table[r_cus])
            if r_cus == len(current_table)-1:
                current_table = current_table[:r_cus]
                r_cus -= 1
            else:
                current_table = current_table[:r_cus]+current_table[r_cus+1:]
            continue

        recent = cache.pop()
        exist_list[recent] = True
        if current_table[r_cus] < recent:
            idx = len(current_table)
            for i in range(r_cus, len(current_table)):
                if recent < current_table[i]:
                    idx = i
                    break
            current_table = current_table[:idx]+[recent]+current_table[idx:]
            continue
        if recent < current_table[r_cus]:
            idx = r_cus
            for i in range(r_cus, -1, -1):
                if current_table[i] < recent:
                    idx = i
                    break
            current_table = current_table[:idx+1]+[recent]+current_table[idx+1:]
            r_cus += 1
            continue


    # print(cache)
    for b in exist_list:
        if b:
            answer += "O"
            continue
        answer += "X"
    return answer
