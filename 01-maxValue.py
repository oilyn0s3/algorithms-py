def max_num(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
    return array[-1]
    
print(max_num([10,9,4,3,7]))