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

    present_cost_even = [math.inf for _ in range(n+1)]
    present_cost_even[start] = 0
    present_cost_odd = [math.inf for _ in range(n+1)]
    present_cost_odd[start] = 0

    visited = [False for _ in range(2*n+1)]
    switch = 0
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if visited[node]:
            continue
        if trap_idx[node]:
            switch += 1
        if switch % 2 == 0:
            for next_node in dictionary[node]:
                if visited[next_node]:
                    continue
                cost = dictionary[node][next_node]
                if present_cost_even[node]+cost < present_cost_even[next_node]:
                    present_cost_even[next_node] = present_cost_even[node]+cost
                queue.append(next_node)
            visited[node] = True
            continue

        for next_node in dictionary[node]:
            if visited[next_node]:
                continue
            cost = dictionary[node][next_node]
            if present_cost_odd[node-n]+cost < present_cost_odd[next_node-n]:
                present_cost_odd[next_node-n] = present_cost_odd[node-n]+cost
            queue.append(next_node)
        visited[node] = True

    if switch % 2 == 0:
        return present_cost_even[end]

    return present_cost_odd[end]
