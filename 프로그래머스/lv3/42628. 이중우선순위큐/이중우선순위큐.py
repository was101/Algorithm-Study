def solution(operations):
    nlist = []
    for i in operations:
        if i[0] == 'I': 
            nlist.append(int(i.split()[1]))
            nlist.sort()
        elif i[0] == 'D':
            if len(nlist) > 0 and i.split()[1] == '1': nlist.pop()
            elif len(nlist) > 0 and i.split()[1] == '-1':nlist.pop(0)
    if len(nlist) < 2: nlist.append(0)
    return [max(nlist), min(nlist)]