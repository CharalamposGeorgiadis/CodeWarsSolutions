import string

def is_pangram(s):
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for character in s.lower():
        if character in a:
            a.remove(character)
    if int(len(a))==0:
        return True
    return False
pass



string=input("Give me a string\n")
if is_pangram(string)==True:
    print("The string is a pangram\n")
else:
    print("The string is not a pangram\n")
