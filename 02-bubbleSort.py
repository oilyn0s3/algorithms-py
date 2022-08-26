def bubble(array):
    for j in range(len(array)-1):

        for i in range(len(array)-j-1):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
        print(f"pass #{j}\n{array}")

    print(f"\nsorted array {array}")

bubble([10,9,4,3,7])