def match(s1, s2):
    cnt = 0
    for x, y in zip(s1,s2):
        if x != y: cnt += 1
        if cnt > 1: return False
    return True if cnt == 1 else False

def solution(begin, target, words):
    
    if target not in words: return 0
    
    answer = 1
    change = []
    for word in words:
        if match(word, begin): change.append(word)
    
    while target not in change:
        cnt = len(change)
        for _ in range(cnt):
            w = change.pop(0)
            for word in words:
                if match(word, w): change.append(word)
        answer += 1
    
    return answer