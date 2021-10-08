def solution(roman):
    number=0
    for i in range(len(roman)):
        if roman[i:i+1]=='M':
            number=number+1000
        elif roman[i:i+1]=='D':
            if roman[i+1:i+2]=='M':
                number=number-500
            else:
                number=number+500
        elif roman[i:i+1]=='C':
            if roman[i + 1:i + 2] == 'D':
                number = number - 100
            elif roman[i + 1:i + 2] == 'M':
                number = number - 100
            else:number=number+100
        elif roman[i:i + 1] == 'L':
            if roman[i + 1:i + 2] == 'C':
                number = number - 50
            elif roman[i + 1:i + 2] == 'D':
                number = number - 50
            elif roman[i + 1:i + 2] == 'M':
                number = number - 50
            else:
                number = number + 50
        elif roman[i:i + 1] == 'X':
            if roman[i + 1:i + 2] == 'L':
                number = number - 10
            elif roman[i + 1:i + 2] == 'C':
                number = number - 10
            elif roman[i + 1:i + 2] == 'D':
                number = number - 10
            elif roman[i + 1:i + 2] == 'M':
                number = number - 10
            else:
                number = number + 10
        elif roman[i:i + 1] == 'V':
            if roman[i + 1:i + 2] == 'X':
                number = number - 5
            elif roman[i + 1:i + 2] == 'L':
                number = number - 5
            elif roman[i + 1:i + 2] == 'C':
                number = number - 5
            elif roman[i + 1:i + 2] == 'D':
                number = number - 5
            elif roman[i + 1:i + 2] == 'M':
                number = number - 5
            else:
                number = number + 5
        elif roman[i:i + 1] == 'I':
            if roman[i + 1:i + 2] == 'V':
                number = number - 1
            elif roman[i + 1:i + 2] == 'X':
                number = number - 1
            elif roman[i + 1:i + 2] == 'L':
                number = number - 1
            elif roman[i + 1:i + 2] == 'C':
                number = number - 1
            elif roman[i + 1:i + 2] == 'D':
                number = number - 1
            elif roman[i + 1:i + 2] == 'M':
                number = number - 1
            else:
                number = number + 1
    return number
    pass



roman=input("give me a roman numeral\n")
print(solution(roman))