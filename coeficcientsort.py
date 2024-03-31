array = [7,5,9,0,3,1,6,2,9,1,4,8,5,0,2]

def cerray(array):

    max = 0
    min = 0
    for data in array:
        if (data > max):
            max = data
        if(data < min):
            min = data
 
    array2 = [0 for _ in range(max+1)]

    for i in range(len(array)):
        array2[array[i]] = array2[array[i]] + 1

    for k in range(len(array2)):
        for j in range(array2[k]):
            print(k,end = ' ')

cerray(array)