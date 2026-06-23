def leangthoflongestsubstring(s):
    seen=set()
    left=0
    max_lrangth=0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1

        seen.add(s[right])
        max_lrangth=max(max_lrangth,right-left+1)
    return  max_lrangth
s="abcdacca"
print(leangthoflongestsubstring(s))