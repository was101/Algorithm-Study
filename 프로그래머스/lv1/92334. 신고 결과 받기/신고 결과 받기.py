def solution(id_list, report, k):
    answer = []
    report_list = dict()
    report_id = []
    for i in id_list:
        report_list[i] = [0]
    for r in report:
        s = r.split()
        if s[1] not in report_list[s[0]]:
            report_list[s[0]].append(s[1])
            report_list[s[1]][0] += 1
        if report_list[s[1]][0] >= k and s[1] not in report_id: report_id.append(s[1])
    idx = 0
    for ls in report_list:
        answer.append(0)
        for re in report_id:
            if re in report_list[ls]:
                answer[idx] += 1
        idx += 1
    return answer

