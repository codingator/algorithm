def solution(answers):
    users = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    score = []
    
    for i in users:
        score.append(0)
            
        for ans in range(len(answers)):
            if answers[ans] == i[ans%len(i)]:
                score[-1] += 1

    return list(filter(lambda e: score[e - 1] == max(score), range(1, len(score) + 1)))