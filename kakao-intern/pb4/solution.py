import math
from collections import deque
from collections import defaultdict

def solution(n, start, end, roads, traps):
    dictionary = defaultdict(dict)
    trap_idx = [False for _ in range(2*n+1)]

    for i in traps:
        trap_idx[i] = True
        trap_idx[i+n] = True

    for route in roads:
        from_, to, cost = route[0], route[1], route[2]
        dictionary[from_][to] = cost
        dictionary[to+n][from_+n] = cost

    present_cost = [math.inf for _ in range(n+1)]
    present_cost[start] = 0

    switch = 0
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node)

        if trap_idx[node]:
            switch += 1
        if switch % 2 == 0:

            if n < node:
                node -= n

            for next_node in dictionary[node]:
                cost = dictionary[node][next_node]
                if present_cost[node]+cost < present_cost[next_node]:
                    present_cost[next_node] = present_cost[node]+cost
                    queue.append(next_node)
            continue
        node += n
        for next_node in dictionary[node]:
            cost = dictionary[node][next_node]
            if present_cost[node-n]+cost < present_cost[next_node-n]:
                present_cost[next_node-n] = present_cost[node-n]+cost
                queue.append(next_node)

    return present_cost[end]
