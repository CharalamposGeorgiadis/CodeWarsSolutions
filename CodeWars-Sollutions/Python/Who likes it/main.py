def likes(names):
    output=''
    if int(len(names))==0:
        output="no one likes this"
    elif int(len(names))==1:
        output=names[0]+ " likes this"
    elif int(len(names)) == 2:
        output = names[0] +" and "+names[1]+  " like this"
    elif int(len(names)) == 3:
        output = names[0] +", "+names[1]+ " and "+names[2]+ " like this"
    else:
        output = names[0] +", "+names[1]+ " and "+ str((len(names)-2))+ " others like this"
    return output
pass





size=int(input("Give me the number of people\n"))
aString=[None]*size
print(len(aString))
for i in range(size):
    aString[i]=input("Give me a name\n")
print(likes(aString))

