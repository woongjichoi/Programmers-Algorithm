from collections import deque

def solution(skill, skill_trees):
    answer=0
    for skill_tree in skill_trees:
        queue=deque(list(skill))
        flag=1
        for st in skill_tree: 
            if len(queue)>0:
                if st==queue[0]:
                    a=queue.popleft()
                elif st in skill and st!=queue[0]:
                    flag=0
                    break
        if flag==0:
            continue
        answer+=1
    return answer
