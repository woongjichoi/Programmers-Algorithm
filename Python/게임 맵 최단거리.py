def solution(maps):
    i=0
    j=0
    distance=[[-1]*len(maps[0]) for _ in range(len(maps))]
    
    from collections import deque
    
    queue=deque()
    queue.append([i,j])
    
    distance[0][0]=1
    
    while queue:
        i_now,j_now=queue.popleft()
        
        # 상하좌우
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        for direction in directions:
            x=i_now+direction[0]
            y=j_now+direction[1]
            
            
            # 진영 벗어나지 않을 때                  
            if 0<=x<len(maps) and 0<=y<len(maps[0]):
                # 갈 수 있는 길일 때
                if maps[x][y]==1:
                    if distance[x][y]==-1:
                        queue.append([x,y])
                        distance[x][y]=distance[i_now][j_now]+1
            
    return distance[-1][-1]

"""실패한 풀이
def solution(maps):
    i=0
    j=0
    distance=1
    visited=[[0]*len(maps[0]) for _ in range(len(maps))]
    
    from collections import deque
    
    queue=deque()
    queue.append([i,j,distance])
    
    while queue:
        i_now,j_now,distance_now=queue.popleft()
        
        # 상하좌우
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        for direction in directions:
            x=i_now+direction[0]
            y=j_now+direction[1]
            
            # 진영 벗어나지 않을 때
            if x<0 or x>len(maps)-1 or y<0 or y>len(maps[0])-1:
                continue
            # 이미 방문했을 때 
            if visited[x][y]==1:
                continue
            # 갈 수 없는 길일 때
            if maps[x][y]==0:
                continue
            
            queue.append([x,y,distance_now+1])
            visited[x][y]=1
            #print(queue)
            
    if i_now==len(maps)-1 and j_now==len(maps[0])-1:
        return distance_now
    else:
        return -1
"""
