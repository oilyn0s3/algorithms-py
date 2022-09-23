def reverse(arr):
    length = len(arr)
    print(arr)
    for index in range(int(length/2)):
        arr[index], arr[length - index - 1] = arr[length - index - 1], arr[index] 
    return arr 
print(reverse([1,2,3,4,5,6]))