def solution(n):
    fib = [0, 1]
    for i in range(2, n):
        fib[0], fib[1] = fib[1], sum(fib)
    return sum(fib) % 1234567