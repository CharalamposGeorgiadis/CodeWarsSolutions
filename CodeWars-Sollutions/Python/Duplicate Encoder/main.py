def duplicate_encode(word):
    final=''
    word=word.lower()
    flag = [None] * int(len(word))
    duplicate = [None] * int(len(word))
    for i in range(int(len(word))):
        if word[i] not in flag:
            flag[i]=word[i]
        else:
            duplicate[i]=word[i]
    for i in range(int(len(word))):
        if word[i] in duplicate:
              flag[i] = ')'
        else:
            flag[i]='('
    for i in range(int(len(word))):
        final=final+flag[i]
    return final
    pass


aString = input("Give me a string\n")
print(duplicate_encode(aString))
