def solution(number):
    sum = 0
    for x in range(number):
        if x % 3 == 0 and x % 5 == 0:
            sum = sum + x
        elif x % 3 == 0:
            sum = sum + x
        elif x % 5 == 0:
            sum = sum + x
    return sum
    pass


size = int(input("Give me a natural number\n"))
final = solution(size)
print(final)
