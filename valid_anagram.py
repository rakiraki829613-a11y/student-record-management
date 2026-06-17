def validanagram(s,t):
    if sorted(s)==sorted(t):
        return True
    else:
        return False
    s="anagram"
    t="nagaram"
    print(validanagram(s,t))