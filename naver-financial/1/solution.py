from collections import defaultdict

visitable = defaultdict(list)

def check_pb_num(student_1, student_2, target_id):
    for key in student_1:
        if visitable[target_id][int(key) - 1]:
            if student_2[key] == student_1[key]:
                continue
        return False
    return True


def solution(logs):
    answer = []
    students = defaultdict(dict)
    student_id = set()

    for log in logs:
        record = log.split(" ")
        students[record[0]][record[1]] = record[-1]
        student_id.add(record[0])
        if not visitable[record[0]]:
            visitable[record[0]] = [False for _ in range(100)]
            visitable[record[0]][int(record[1])-1] = True
            continue
        visitable[record[0]][int(record[1])-1] = True

    student_id = list(student_id)
    visited_id = defaultdict(bool)
    for i in range(len(student_id)-1):
        length_1 = len(students[student_id[i]])
        if length_1 < 5:
            continue
        check = False
        for j in range(i+1, len(student_id)):
            if visited_id[student_id[j]]:
                continue
            length_2 = len(students[student_id[j]])
            if length_1 == length_2 and check_pb_num(students[student_id[i]], students[student_id[j]], student_id[j]):
                check = True
                answer.append(student_id[j])
                visited_id[student_id[j]] = True
        if visited_id[student_id[i]]:
            continue
        if check:
            visited_id[student_id[i]] = True
            answer.append(student_id[i])

    if not answer:
        return ["None"]

    return sorted(answer)
