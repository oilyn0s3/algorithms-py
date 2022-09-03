test_array = [10,9,4,3,7,45,8,1]
print(f"Original Array: \n{test_array}")


def array_append(array,value):
    length = len(array)
    new_array = [0 for i in range(length+1)]

    for i in range(length):
        new_array[i] = array[i]

    new_array[length] = value
    print(new_array)

array_append(test_array,69)


def array_insert(array, index, value):
    length = len(array)
    new_array = [0 for i in range(length + 1)]

    for i in range(index):
        new_array[i] = array[i]
    
    for j in range(index, length):
        new_array[j + 1] = array[j]
    
    new_array[index] = value
    print(new_array)

array_insert(test_array, 3, 69)


def array_delete(array, index):
    length = len(array)
    new_array = [0 for i in range(length - 1)]

    for i in range(index):
        new_array[i] = array[i]
    
    for j in range(index + 1, length):
        new_array[j-1] = array[j]
    
    print(new_array)

array_delete(test_array,0)