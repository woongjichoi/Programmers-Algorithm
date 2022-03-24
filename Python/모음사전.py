from itertools import product

def solution(word):
    answer=0
    alphabet1=['A','E','I','O','U']
    alphabet2=list(map(list, product("AEIOU",repeat=2)))
    alphabet3=list(map(list, product("AEIOU",repeat=3)))
    alphabet4=list(map(list, product("AEIOU",repeat=4)))
    alphabet5=list(map(list, product("AEIOU",repeat=5)))
    l=alphabet1+alphabet2+alphabet3+alphabet4+alphabet5
    for i in range(len(l)):
        l[i]=''.join(l[i])
    l.sort()
    return l.index(word)+1
