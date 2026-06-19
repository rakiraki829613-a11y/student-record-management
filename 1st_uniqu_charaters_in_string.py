def uniquecharates(s):
    freq={}
    for ch in s:
         freq[ch] = freq.get(ch,0)+1

    for i in range(len(s)):
         freq[s[i]]==1
         return i
    return -1
s="leetcode"
print(uniquecharates(s))     


