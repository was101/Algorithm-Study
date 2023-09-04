def solution(s):
    d = {"(":1, ")":-1}
    num = 0
    for st in s:
        num += d[st]
        if num < 0:
            return False
    return num == 0