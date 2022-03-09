def solution(number, k):
    stack=[]
    for n in number:
        while len(stack)>0 and n>stack[-1] and k>0:
            stack.pop()
            k-=1
        stack.append(n)
    if len(stack)>len(number)-k:
        stack=stack[:len(number)-k]
    return ''.join(stack)
