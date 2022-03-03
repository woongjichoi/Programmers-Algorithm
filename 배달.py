def dijkstra(distance, adj):
    import heapq
    heap=[]
    heapq.heappush(heap, [0,1])
    
    while heap:
        cost, node = heapq.heappop(heap)
        for c, n in adj[node]:
            if cost+c < distance[n]:
                distance[n] = cost+c
                heapq.heappush(heap, [distance[n],n])

def solution(N, road, K):
    answer=0
    distance=[float('inf')]*(N+1)
    distance[1]=0
    adj=[[] for _ in range(N+1)]
    for r in road:
        adj[r[0]].append([r[2],r[1]])
        adj[r[1]].append([r[2],r[0]])
    dijkstra(distance, adj)
    for i in range(1,N+1):
        if distance[i]<=K:
            answer+=1
    return answer
