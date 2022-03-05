def solution(clothes):
    answer=1
    d={}
    for cloth in clothes:
        if cloth[-1] not in d:
            d[cloth[-1]]=[cloth[0]]
        else:
            d[cloth[-1]].append(cloth[0])
    for key in d:
        answer*=len(d[key])+1
    return answer-1
