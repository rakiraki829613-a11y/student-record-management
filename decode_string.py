def decoderstring(s):
    stack=[]
    currentstring=""
    currentnum=0
    for ch in s:
        if ch.isdigit():
            currentnum=currentnum*10+int(ch)
        elif ch=='[':
            stack.append((currentstring,currentnum))
            currentstring="" 
            currentnum=0
        elif ch==']':
            prevestring,num=stack.pop()
            currentstring=prevestring+num*currentstring
        else:
            currentstring+=ch
    return currentstring

s="3[a]2[bc]" 
print(decoderstring(s))           