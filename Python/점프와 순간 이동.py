def solution(n):
    answer=0
    while n>0: 
        if n%2==0:
            n=n//2
        else:
            n-=1
            answer+=1
    return answer

    # 1. DP(bottom-up): 정확성 통과O, 효율성 통과X
    # DP 배열에 그 칸까지 건전지 사용량의 최솟값 저장
    #dp=[0]*(n+1)
    #dp[1]=1
    #for i in range(2,n+1):
        #if i%2==0: # 2의 배수인 애는 약수로 바로 가능
            #dp[i]=dp[i//2]
        #else: # 2의 배수가 아닌 애는 바로 전 +1로 가능
            #dp[i]=dp[i-1]+1
    #return dp[n]
    
    # 2. DP(top-bottom): 정확성 통과O, 효율성 통과X
    #dp=[0]*(n+1)
    #while n>0: 
        #if n%2==0:
            #dp[n//2]=dp[n]
            #n=n//2
        #else:
            #dp[n-1]=dp[n]+1
            #n-=1
    #return dp[0]
