def first_non_repeating_letter(string):
    c=0
    flagList=[None]*len(string)
    while True:
        first=string[c:c+1]
        flag=0
        for i in range(c+1, len(string)):
             if first.lower()==string[i:i+1].lower() :
                    flag=1
        if flag==0 and  not(first.lower() in flagList):
            return first
        flagList[c] = first.lower()
        c=c+1
        if c==len(string):
            return ''
    pass


aString = input("Give me a string\n")
print(first_non_repeating_letter(aString))
