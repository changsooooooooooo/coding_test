def solution(n):
    answer = 0
    start, end = 0, 1
    nums = [i+1 for i in range(n)]

    if len(nums) == 1:
        return 1

    current_num = nums[start]+nums[end]
    while start < len(nums) and end < len(nums):
        if current_num == n:
            answer += 1
            current_num -= nums[start]
            start += 1
            continue
        if n < current_num:
            current_num -= nums[start]
            start += 1
            continue
        if current_num < n:
            end += 1
            current_num += nums[end]

    return answer

print(solution(15))
