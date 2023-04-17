import heapq
from collections import deque

def solution(operations):
    tasks = deque([(int(x[2:]), x[0]) for x in operations])
    answer = []
    
    while tasks:
        proc = tasks.popleft()
        if proc[1] == 'I':
            heapq.heappush(answer, proc)
        elif answer:
            if proc[0] > 0:
                answer.sort(reverse=True)
                heapq.heappop(answer)
            else:
                heapq.heappop(answer)

    answer = deque(sorted([x[0] for x in answer]))
    return [answer.pop(), answer.popleft()] if answer else [0, 0]