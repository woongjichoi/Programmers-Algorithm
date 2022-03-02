def solution(s):
    answer=0
    for i in range(len(s)):
        str_now=s[i:]+s[:i]
        stack=[]
        is_right=1
        
        for j in str_now:
            if j=="[" or j=="(" or j=="{":
                stack.append(j)
            elif j=="]":
                if len(stack)>0 and stack[-1]=="[":
                    stack.pop()
                else:
                    is_right=0
                    break
            elif j==")":
                if len(stack)>0 and stack[-1]=="(":
                    stack.pop()
                else:
                    is_right=0
                    break
            elif j=="}":
                if len(stack)>0 and stack[-1]=="{":
                    stack.pop()
                else:
                    is_right=0
                    break
                    
        if len(stack)==0 and is_right==1:
            answer+=1
            
    return answer
