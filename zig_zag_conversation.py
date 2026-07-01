def zigzagconversation(s,numrows):
    if numrows==1 or numrows>=len(s):
        return s
    rows=[""]*numrows
    current_row=0
    direction=1
    for ch in s:

        rows[current_row]+=ch

        if current_row==0:
            direction=1
        elif current_row==numrows-1:
            direction=-1
        current_row+=direction
    return"".join(rows) 
s="PALAGHAJHS"
numrows=3
print(zigzagconversation(s,numrows))       

