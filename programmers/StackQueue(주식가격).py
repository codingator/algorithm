def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            answer[i] += 1
            
            if prices[i] > prices[j]:
                break
    
    return answer
'''
스택/큐와 IO가 필요 없을 땐 참조, 비교만 하는 것이 빠름
'''
# from collections import deque

# def solution(prices):
#     tasks = deque(prices)
#     answer = []
    
#     while len(tasks) > 1:
#         price = tasks.popleft()
        
#         for life in range(len(tasks)):
#             if price > tasks[life]:
#                 break
                
#         answer.append(life + 1)
#         life = 0
        
#     answer.append(life)
#     return answer