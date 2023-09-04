def solution(n):
    answer, idx = 0 , 1
    while idx <= n:
        num = 0
        for i in range(idx, n+1):
            num += i
            if num == n: answer += 1
            if num >= n: break
        idx += 1
    return answer