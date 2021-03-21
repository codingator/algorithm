def solution(board, moves):
    answer = 0
    box = [0]
    
    for i in moves:
        for j in board:
            if j[i - 1] > 0:
                if box[-1] == j[i - 1]:
                    box.pop()
                    answer += 2
                else:
                    box.append(j[i - 1])
                j[i - 1] = 0
                break 
                
    return answer