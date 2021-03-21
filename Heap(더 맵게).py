from heapq import heapify, heappushpop, heappop

def solution(scoville, K):
    heapify(scoville)
    answer = 0
    
    # while K >= scoville[0] and scoville[1]: # RuntimeError(1, 3, 8, 14)
    # while K >= nsmallest(2, scoville)[0]: # performance is lower
    while True:
        if K >= scoville[0] and len(scoville) > 1:
            heappushpop(scoville, heappop(scoville) + (scoville[0] * 2))
            answer += 1
        else:
            break
        
    return -1 if not scoville[0] >= K else answer