def increment_string(strng):
    if len(strng) == 0:
        return '1'
    else:
        if strng[len(strng) - 1].isalpha():
            newString = strng + '1'
        elif strng[len(strng) - 1].isdigit() and len(strng) == 1:
            return str(int(strng[len(strng) - 1]) + 1)
        elif strng[len(strng) - 1].isdigit():
            i = len(strng) - 1
            temp = int(strng[len(strng) - 1]) + 1
            while (True):
                if strng[i - 1].isdigit() and int(strng[i - 1]) == 0:
                    if int(strng[i]) == 9:
                        return strng[0:i - 1] + str(temp)
                    else:
                        return strng[0:i] + str(temp)
                elif strng[i - 1].isdigit() and int(strng[i]) == 9:
                    temp = int(str(strng[i - 1]) + str((len(strng) - i) * '0')) + temp
                elif strng[i - 1].isdigit():
                    break
                elif strng[i - 1].isalpha():
                    break
                i = i - 1
            newString = strng[0:i] + str(temp)
        return newString


aString = input("Give me a string\n")
print(increment_string(aString))
