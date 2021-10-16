def binary(candidate, registered_list):
    mid = len(registered_list)//2
    low, high = 0, mid
    while low<mid or high<len(registered_list):
        if candidate == registered_list[low]:
            return False
        if high == len(registered_list):
            continue
        if candidate == registered_list[high]:
            return False
        low += 1
        high += 1
    return True


def solution(registered_list, new_id):
    answer = ''

    if binary(new_id, registered_list):
        return new_id

    # idx = -1
    # for i, c in enumerate(new_id):
    #     if c.isdecimal():
    #         idx = i
    #         break
    #
    # if idx<0:
    #     idx = len(new_id)
    #     number_part = 1
    #     answer = new_id
    # else:
    #     number_part = int(new_id[idx:len(new_id)])+1
    #     answer = new_id[:idx]+str(number_part)
    #
    # while True:
    #     if binary(answer, registered_list):
    #         return answer
    #     number_part+=1
    #     answer = answer[:idx]+str(number_part)
    #
    #
    # return answer
