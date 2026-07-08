def issubsequence(s, t):

    i = 0
    j = 0

    while i < len(s) and j < len(t):

        # characters match
        if s[i] == t[j]:

            i += 1

        # always move j
        j += 1

    return i == len(s)


s = "abc"
t = "ahbgdc"

print(issubsequence(s, t))