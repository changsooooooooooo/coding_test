def solution(numArr):
    answer = []

    avg = round(sum(numArr)/len(numArr), 2)

    if 90<=avg:
        return ["{:.2f}".format(avg), "A"]
    if 80<=avg<90:
        return ["{:.2f}".format(avg), "B"]
    if 70<=avg<80:
        return ["{:.2f}".format(avg), "C"]
    if 60<=avg<70:
        return ["{:.2f}".format(avg), "D"]

    return ["{:.2f}".format(avg), "F"]
