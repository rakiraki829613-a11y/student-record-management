def usageofcapital(s):
    if s.uppercase():
        return True
    if s.lowercase():
        return True
    if s[0].uppercase() and s[1:].lowercase():
        return True
    
    return False
s="Ieetcode"
print(usageofcapital(s))