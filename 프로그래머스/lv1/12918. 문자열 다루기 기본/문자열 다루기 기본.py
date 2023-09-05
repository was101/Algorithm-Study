def solution(s):
    num = '01234526789'
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i not in num:
                return False
        return True
    return False

def solution(s):
    return len(s) in [4, 6] and s.isdigit()