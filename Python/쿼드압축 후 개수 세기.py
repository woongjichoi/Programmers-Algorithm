def solution(arr):
    n=len(arr)
    answer=[0,0]
    
    def checkCompressed(x,y,n):
        init=arr[x][y]
        for i in range(x,x+n):
            for j in range(y,y+n):
                if init!=arr[i][j]:
                    n=n//2
                    checkCompressed(x,y,n)
                    checkCompressed(x+n,y,n)
                    checkCompressed(x,y+n,n)
                    checkCompressed(x+n,y+n,n)
                    return
        answer[init]+=1

    checkCompressed(0,0,n)
    return answer
