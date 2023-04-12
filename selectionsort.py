def selectionsort(array, size):
    for step in range(size):
        min_ind = step
        for i in range(step+1, size):
            if array[i] < array[min_ind]:
                min_ind = i
        (array[step], array[min_ind]) = (array[min_ind], array[step])
data = [2,3,24,224,2]
size = len(data)
selectionsort(data, size)
print(data)