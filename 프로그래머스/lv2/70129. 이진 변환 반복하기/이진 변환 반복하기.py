def solution(s):
    answer = [0, 0]
    while s != '1':
        st = ''
        answer[0] += 1
        for x in s:
            if x == '0': answer[1] += 1
            else: st += x
        s = str(bin(len(st)))[2:]
    return answer
                