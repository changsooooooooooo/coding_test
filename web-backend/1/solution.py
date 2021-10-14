def solution(lottos, win_nums):
    answer = []

    min_equal, zero_count = 0, 0
    for l in lottos:
        if l in win_nums:
            min_equal += 1
        if not l:
            zero_count += 1

    min_rank = min(7-min_equal, 6)
    max_rank = min(7-min_equal-zero_count, 6)

    return [max_rank, min_rank]
