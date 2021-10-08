def sort_array(source_array):
    for i in range(len(source_array)):
        if not(source_array[i]%2==0):
            for j in range(i+1,len(source_array)):
                if not(source_array[j]%2==0) and source_array[i]>source_array[j]:
                    temp=source_array[i]
                    source_array[i] = source_array[j]
                    source_array[j]=temp
    return source_array
    # Return a sorted array.



size=int(input("Give me the size of the array\n"))
a=[0]*size
for i in range(size):
    a[i]=int(input("Give me a number\n"))

print(sort_array(a))