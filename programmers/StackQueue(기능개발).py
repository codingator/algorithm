def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if not Q or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

# from collections import deque

# def solution(progresses, speeds):
#     tasks = deque(progresses)
#     answer = []
#     cnt = 0
    
#     while tasks:
#         if tasks[0] >= 100:
#             answer.append(0)
            
#             for _ in range(len(tasks)):
#                 if tasks[0] >= 100:
#                     answer[-1] += 1
#                     tasks.popleft()
#                 else:
#                     break
#         else:
#             tasks = deque(tasks[x] + speeds[x + (len(speeds) - len(tasks))] for x in range(len(tasks)))
        
#     return answer