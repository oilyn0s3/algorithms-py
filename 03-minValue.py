def min_value(array):
    min_index = 0
    for i in range(1,len(array)-1):
        if array[min_index] > array[i]:
            min_index = i
            i += 1
        else:
            i += 1
    print(f'min value: {array[min_index]}')
min_value([10,9,4,3,7])