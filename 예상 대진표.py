import math
def solution(n,a,b):
    answer=0
    while a!=b: # 이렇게 문제에서 매개변수로 주어진 변수 써도 됨 
        a=math.ceil(a/2)
        b=math.ceil(b/2)
        answer+=1
    return answer

    ####### 다른 사람 풀이 (math.ceil -> +1하고 //2)
    #answer=0
    #while a!=b:
        #a=(a+1)//2
        #b=(b+1)//2
        #answer+=1
    #return answer
