from collections import deque

def solution(bridge_length, weight, truck_weights):
    tasks = deque([x for x in truck_weights])
    proc = deque([0 for _ in range(bridge_length)])
    time = stack = 0
    
    while proc:
        if proc[0] > 0:
            stack -= proc[0]
            
        time += 1
        proc.popleft()
        
        if tasks:
            if (stack + tasks[0]) <= weight:
                stack += tasks[0]
                proc.append(tasks.popleft())
            else:
                proc.append(0)
        
    return time