def solution(citations):
    answer=0
    citations.sort(reverse=True)
    for h in range(citations[0],-1,-1):
        if h in citations:
            tmp=citations.index(h)+1
        if tmp>=h:
            answer=h
            break
    return answer
                
