def accum(s):
    s=s.upper()
    temp=s[0]+"-"
    for i in range(1,len(s)):
        if i!=len(s)-1:
            temp=temp+s[i]+i*s[i].lower()+"-"
        else:
            temp = temp + s[i] + i * s[i].lower() + ""
    return temp
    pass

aString = input("Give me a string\n")
print(accum(aString))
