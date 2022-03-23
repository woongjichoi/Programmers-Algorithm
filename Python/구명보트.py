from collections import deque

def solution(people, limit):
    answer=0
    people.sort(reverse=True) 
    queue=deque(people)
    while queue:
        if len(queue)==1:
            answer+=1
            break
        if queue[0]+queue[-1]<=limit: # 그리디 -> 제일 무거운 애랑 제일 가벼운 애를 봐야 함 
            queue.popleft()
            queue.pop()
        else:
            queue.popleft()
        answer+=1
    return answer

# 1. 리스트로 큐 구현 -> 시간 초과
# 2. deque는 중간을 못 뺀다고 생각했는데 deque도 remove 가능했음 -> 시간 초과 
# 3. 최대한 쓸데없는 프로세스를 줄이는 식으로 
