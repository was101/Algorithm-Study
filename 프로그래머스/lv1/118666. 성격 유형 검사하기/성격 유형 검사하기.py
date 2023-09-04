def solution(survey, choices):
    answer = ''
    survey_list = ["RT", "TR", "CF", "FC", "JM", "MJ", "AN", "NA"]
    at = [0, 0, 0, 0]
    
    for idx, sur in enumerate(survey):
        
        point = choices[idx] - 4
        
        if survey_list.index(sur) % 2: at[survey_list.index(sur) // 2] += point
        
        else: at[survey_list.index(sur) // 2] -= point
        
    for idx, pnt in enumerate(at):
        
        answer += survey_list[idx*2][1-(pnt>=0)]
        
    return answer