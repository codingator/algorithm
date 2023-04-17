def solution(grid):
    answer = []
    # paths = []
    
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
                answer += find_cycle(grid, [], f'{y}{x}', f'{y}{x}')
                # find_cycle(grid, [], f'{y}{x}', f'{y+1}{x}')
                # find_cycle(grid, [], f'{y}{x}', f'{y+2}{x}')
                # find_cycle(grid, [], f'{y}{x}', f'{y}{x+1}')
                # find_cycle(grid, [], f'{y}{x}', f'{y}{x+2}')
#             시작 방향이 없음. 3파라미터를 다음으로 잡음
#     ** paths에 이진으로 넣어서 탐색 속도 감소
#     1. '진행 방향'과 '진행 경로'를 알아야 함.
#     2. 이전/현재 x, y를 기반으로 방향 구하기?
#     3. 시작 == 현재 > length return, 앞 != and 현재 in paths > pass
#     4. paths 초기화, 반복? 언제까지?? 시작 위치/방향은?
    print(answer)
    return answer

def find_cycle(grid, paths, p, c):
    paths.append(p)
    
    if paths[0] == c:
#       or (y*10)+x
#       조건을 c의 next가   ㅝㄴ소리고
        return len(paths)
    elif c in paths:
        return

    
#     1. 방향구함 2. 현재 위치 SLR 다음 방향 더해 줌
    y = int(p[0])-int(c[0])
    x = int(p[1])-int(c[1])
    
    if y != 0:
        if y > 0:
            if grid[int(c[0])][int(c[1])] == 'L':
                x = 1
            elif grid[int(c[0])][int(c[1])] == 'R':
                x = -1
        else:
            if grid[int(c[0])][int(c[1])] == 'L':
                x = -1
            elif grid[int(c[0])][int(c[1])] == 'R':
                x = 1
        y = 0
    elif x != 0:
        if x > 0:
            if grid[int(c[0])][int(c[1])] == 'L':
                y = 1
            elif grid[int(c[0])][int(c[1])] == 'R':
                y = -1
        else:
            if grid[int(c[0])][int(c[1])] == 'L':
                y = -1
            elif grid[int(c[0])][int(c[1])] == 'R':
                y = 1
        x = 0
    
    
    y += int(c[0])
    x += int(c[1])
    find_cycle(grid, paths, c, f'{y%len(grid)}{x%len(grid[y])}')