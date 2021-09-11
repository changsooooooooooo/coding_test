from collections import defaultdict

def solution(research, n, k):
    answer = list()
    issue_dict = defaultdict(dict)
    date_num = 1
    for r in research:
        temp_dict = defaultdict(int)
        for alpha in r:
            temp_dict[alpha] += 1
        for key in temp_dict:
            issue_dict[key][date_num] = temp_dict[key]
        date_num += 1

    for key in issue_dict:
        temp_dict = defaultdict(int)
        for i in range(len(research)):
            if i+1 not in issue_dict[key]:
                temp_dict[i+1] = 0
                continue
            temp_dict[i+1] = issue_dict[key][i+1]
        issue_dict[key] = temp_dict

    for key in issue_dict:
        total = 0
        for i in range(len(research)-n+1):
           temp, check = 0, True
           for j in range(n):
               if issue_dict[key][i+j+1]<k:
                   check = False
                   break
               temp += issue_dict[key][i+j+1]
           if not check:
               break
           if 2*n*k<=temp:
               total+=1
               answer.append([total, key])
    answer.sort(key=lambda x : (-x[0], x[1]))

    if not answer:
        return "None"

    return answer[0][1]
