def solution(s):
    # s가 set이 아닌 str인 게 처음에 당황함  
    answer=[]
    s=s[2:-2]
    s=s.split("},{") # 처음에는 "},"로 split해서 ['2', '{2,1', '{2,1,3', '{2,1,3,4'] 이렇게 됐는데 애매한 {까지 없앨 생각 왜 못했는지 ㅠㅠ 
    s.sort(key=lambda x:len(x)) 
    for item in s:
        temp=item.split(",")
        for t in temp:
            if t not in answer: 
                # 처음에는 ["2", "21", "213"] 이런 식일 때 첫번째 원소 넣고 그 다음부터는 붙어있는 두개의 차집합을 넣으려고 했었는데 그렇게 말고 그냥 ["2","2,1","2,1,3"]에서 not in으로 
                answer.append(t)
    answer=list(map(int, answer))
    return answer
