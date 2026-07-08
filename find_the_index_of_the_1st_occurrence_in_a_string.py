def firstoccurenceofthestring(haystack,needle):
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)]==needle:
            return i
    return -1
haystack="hellow"
needle="ll"
print(firstoccurenceofthestring(haystack,needle))