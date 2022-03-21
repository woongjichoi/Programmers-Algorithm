def solution(n, words):
    now=0 # 현재 누구 차례인지 
    last_word="" # 앞사람이 말한 단어의 마지막 문자
    used_words=[] # 이미 등장한 단어들 저장 
    
    turn=[]
    for j in range(n):
        turn.append(j) 
        
    for i in range(len(words)):
        now=turn[i%n] # 여기가 핵심! ★
        if len(words[i])<=1 or words[i] in used_words:
            return [now+1,(i//n)+1]
        if i>0 and last_word!=words[i][0]:
            return [now+1,(i//n)+1]
        last_word=words[i][-1]
        used_words.append(words[i])
    return [0,0]
