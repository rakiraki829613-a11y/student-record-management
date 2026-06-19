def lastleangthofword(s):
    s=s.split()
    return len(s[-1])
s="hello world"
print(lastleangthofword(s))