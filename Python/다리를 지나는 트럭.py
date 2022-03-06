# 0의 역할 ★

def solution(bridge_length, weight, truck_weights):
    time=0
    bridge=[0]*bridge_length
    while bridge:
        bridge.pop(0)
        time+=1
        if len(truck_weights)>0:
            if sum(bridge)+truck_weights[0]<=weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return time
