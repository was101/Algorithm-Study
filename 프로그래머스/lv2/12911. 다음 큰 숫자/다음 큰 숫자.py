def solution(n):
    num = n
    while True:
        num = num + 1
        if str(bin(n))[2:].count('1') == str(bin(num))[2:].count('1'):
            return num