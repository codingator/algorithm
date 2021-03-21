def solution(priorities, location):
    tasks = [(y, x) for x, y in enumerate(priorities)]
    answer = 0    
    while tasks:
        cur = tasks.pop(0)
        if any(cur[0] < task[0] for task in tasks):
            tasks.append(cur)
        else:
            answer += 1
            if cur[1] == location:
                return answer

# 10% ~ 20% 정도 느림
# from collections import deque

# def solution(priorities, location):
#     tasks = deque([[y, x] for x, y in enumerate(priorities)])
#     answer = 0
    
#     while tasks:
#         if any(tasks[0][0] < q[0] for q in tasks):
#             tasks.rotate(-1)
#         else:
#             answer += 1     
#             if tasks.popleft()[1] == location:
#                 return answer