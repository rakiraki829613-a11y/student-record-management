def romantointeger(s):
    roman={
        'l':1,
        'v':5,
        'x':10,
        'l':50,
        'c':100,
        'd':500,
        'm':1000
    }
    total=0
    for i in range(len(s)-1):
        if roman[s[i]]<roman[s[i+1]]:
            total-=roman[s[i]]

        else:
            total+=roman[s[i]]

    total+=roman[s[-1]]
    return total
s="mx"
print(romantointeger(s))
         
