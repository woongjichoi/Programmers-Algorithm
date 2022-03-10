def solution(k, dungeons):
    from itertools import permutations
    tmp=list(permutations(dungeons,len(dungeons)))
    result=0
    for t in tmp:
        answer=0
        fatigue=k
        for d in t:
            if fatigue>=d[0]:
                fatigue-=d[1]
                answer+=1
        if answer>result:
            result=answer
    return result
