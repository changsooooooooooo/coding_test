from collections import defaultdict, deque

def search(start, money, graph, money_graph):
    queue = deque([(start, money)])
    money_graph[start] += money

    while queue:
        node, money = queue.popleft()

        if node == "center":
            break

        need_to_give = int(money*0.1)
        next_node = graph[node]
        money_graph[next_node] += need_to_give
        money_graph[node] -= need_to_give
        queue.append((next_node, need_to_give))


def solution(enroll, referral, seller, amount):
    answer = []
    graph = defaultdict(str)
    money_graph = defaultdict(int)

    for e in enroll:
        graph[e] = ""
        money_graph[e] = 0

    money_graph["center"] = 0
    for idx, r in enumerate(referral):
        if r == "-":
            graph[enroll[idx]] = "center"
            continue
        graph[enroll[idx]] = r

    for idx, sell in enumerate(seller):
        search(sell, amount[idx]*100, graph, money_graph)

    for e in enroll:
        answer.append(money_graph[e])

    return answer
