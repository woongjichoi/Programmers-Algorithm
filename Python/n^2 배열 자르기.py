def solution(n, left, right):
    def findNumber(i,j): # 2차원 배열 인덱스가 주어졌을 때 숫자 구하는 함수
        # 규칙을 너무 어렵게 생각함 i=0, j=0, i=n-1, j=n-1, 그 외
        # 이렇게 나누어 생각했는데 그냥 i,j 둘 중 큰 값 따라가는 것이었음
        return max(i,j)+1
    
    answer=[]
    for i in range(int(left), int(right)+1): # 왜 int 씌우는지 모름 
        a=i//n
        b=i%n
        answer.append(findNumber(a,b))
    return answer
