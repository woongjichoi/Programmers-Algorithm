from collections import deque

def solution(prices):
    answer=[]
    queue=deque(prices)
    while queue: 
        flag=True
        tmp=0
        now=queue.popleft()
        for q in queue:
            if now>q:
                flag=False
                break
            elif now<=q:
                tmp+=1 
        if flag==False:
            answer.append(tmp+1)
        else:
            answer.append(tmp)
    return answer

# 한 번이라도 if문 갔을 때랑 아예 elif만 갔을 때 차이가 append할 값이 달라서
# flag 처리했는데 그렇게 안 하고 tmp+=1한 다음에 break하는 식으로 하면 통일됨 
