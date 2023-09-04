def solution(n, works):
    work = {}
    
    for num in works:
        if num not in work.keys(): work[num] = 1
        else: work[num] += 1
    keys = sorted(work.keys(), reverse=True)
    
    for _ in range(n):
        if keys[0] == 0: break
        work[keys[0]] -= 1
        if keys[0] - 1 not in work.keys():
            work[keys[0] - 1] = 1
            keys.append(keys[0] - 1)
            keys.sort(reverse=True)
        else: work[keys[0] - 1] += 1
        if work[keys[0]] == 0: keys.pop(0)
    
    return sum((x ** 2) * y for x, y in work.items())