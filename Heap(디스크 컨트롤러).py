import heapq
from collections import deque

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0
    while q:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while tasks and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if tasks and not q:
            heapq.heappush(q, tasks.popleft())
    return total_response_time // len(jobs)