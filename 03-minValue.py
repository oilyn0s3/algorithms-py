def min_value(array):
    
    min_index = 0
    for i in range(1,len(array)):
        if array[min_index] > array[i]:
            min_index = i

    print(f'min value: {array[min_index]}')
    
min_value([10,9,4,3,7,45,8,1])