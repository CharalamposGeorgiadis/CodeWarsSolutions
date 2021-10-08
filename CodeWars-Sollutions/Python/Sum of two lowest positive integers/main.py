def sum_two_smallest_numbers(numbers):
    min1 = min(numbers)
    del numbers[numbers.index(min1)]
    min2 = min(numbers)
    while min2==min1:
        del numbers[numbers.index(min2)]
        min2 = min(numbers)
    return int(min1) + int(min2)
    pass


size = input("Give me an integer larger than 3\n")
size = int(size)
a = [0] * size
for i in range(size):
    a[i] = input("Give me a positive number\n")
final = sum_two_smallest_numbers(a)
print(final)
