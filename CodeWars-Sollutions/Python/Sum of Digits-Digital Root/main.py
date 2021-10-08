def digital_root(n):
    while True:
        s=0
        for character in str(n):
            s = s + int(character)
        n=s
        if (len(str(s))) == 1:
            break
    return s
    pass


aNumber = input("Give me a number\n")
sum = digital_root(aNumber)
print(sum)
