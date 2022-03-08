def solution(brown, yellow):
    import math
    #h**2-h*((brown/2)+2)+brown+yellow=0
    w=((brown/2+2)+math.sqrt((brown/2+2)**2-4*(brown+yellow)))/2
    h=((brown/2+2)-math.sqrt((brown/2+2)**2-4*(brown+yellow)))/2
    return [w,h]
