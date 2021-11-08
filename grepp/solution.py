def solution(customer, K):
    answer = []
    visited = [False for _ in range(1000000)]
    cand_idx = [[len(customer)+1, i] for i in range(1000000)]
    for i, c in enumerate(customer):
        if c[1]:
            visited[c[0]-1] = True
            cand_idx[c[0]-1][0] = i
            continue
        if visited[c[0]-1]:
            visited[c[0]-1] = False
            cand_idx[c[0]-1][0] = len(customer)+1

    cand_idx = sorted(cand_idx)
    idx = 0
    while 0<K:
        if len(customer)<cand_idx[idx][0]:
            break
        answer.append(cand_idx[idx][1]+1)
        idx+=1
        K-=1

    return sorted(answer)
