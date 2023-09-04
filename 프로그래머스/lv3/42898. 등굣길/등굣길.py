def solution(m, n, puddles):
    
    road = [[0 for _ in range(m)] for _ in range(n)]
    road[0][0] = 1
    
    for x in range(n):
        for y in range(m):
            if [y + 1, x + 1] in puddles:
                road[x][y] = 0
            if x + 1 <= n - 1: road[x+1][y] += road[x][y]
            if y + 1 <= m - 1: road[x][y+1] += road[x][y]
    return road[-1][-1] % 1000000007