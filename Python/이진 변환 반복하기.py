def binaryChange(c):
    stack=[]
    while c>0:
        stack.append(c%2)
        c=c//2
    stack=list(map(str,stack))
    return ''.join(stack)
    
def solution(s):
    count_zero=0
    count_change=0
    while True:
        if s=="1":
            break
        temp=""
        for i in range(len(s)):
            if s[i]=="0":
                count_zero+=1
            elif s[i]=="1":
                temp+=s[i]
        c=len(temp)
        s=binaryChange(c)
        count_change+=1
    
    return [count_change,count_zero]
