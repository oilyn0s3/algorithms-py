def selection(array):

    for i in range(len(array)):
        min_index = i
        
        for j in range(i+1, len(array)):
            if array[j] < array[min_index] :
                min_index = j

        if min_index != i:            
          array[min_index],  array[i] = array[i], array[min_index]

    print(array)

selection([10,9,4,3,7,45,8,1])
