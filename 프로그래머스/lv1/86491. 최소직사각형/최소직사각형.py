def solution(sizes):
    x, y = 0, 0
    for i in sizes:
        x = max(x, sorted(i)[0])
        y = max(y, sorted(i)[1])
    return x*y