from collections import deque

def solution(cacheSize, cities):
    if cacheSize==0:
        return 5*len(cities)
    answer=0
    queue=deque([])
    for i in range(len(cities)):
        cities[i]=cities[i].lower()
    for city in cities:
        if city not in queue:
            if len(queue)==cacheSize:
                temp=queue.popleft()
            queue.append(city)
            answer+=5
        else:
            queue.remove(city)
            queue.append(city)
            answer+=1
    return answer
