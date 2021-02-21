import collections

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

graph = dict()
answer = collections.deque()

for ticket in tickets:
    if ticket[0] in graph:
        graph[ticket[0]].append(ticket)
    else:
        graph[ticket[0]] = [ticket]

visited = [False for _ in range(len(tickets))]

start = 0



