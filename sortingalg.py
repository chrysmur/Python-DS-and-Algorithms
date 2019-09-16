array = [99,44,6,2,1,5,63,87,283,4,0]
print(array)

#Bubble Sort
def BubbleSort(array):
    for i in range(len(array)-1):    
        for j in range(len(array)-1):
            temp = array[j+1]
            if array[j] > temp:
                array[j+1]= array[j]
                array[j] = temp

    return array


#Selection sort
def SelectionSort(array):
    for i in range(len(array)-1): 
        mini = array[i]   
        for j in range(i+1,len(array)):            
            if array[j] < mini:
                temp=mini
                mini = array[j]
                array[j] = temp
        array[i] = mini
    return array

def InsertionSort(array):
    for i in range(1,len(array)):
        j = i
        while j>0:
            if array[j]< array[j-1]:
                temp = array[j]
                array[j]= array[j-1]
                array[j-1] =temp
            j-=1
    return array

def mergeSort(array):
    if len(array) == 1:
        return array
    length = len(array)
    left = array[:length//2]
    right = array[length//2:]

    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    for i in range(len(left)):
        for i in range(len(right)):
            if left[i] < right[i]:
                print(left[i])
    

print("Bubble Sort")
print(BubbleSort(array))
print("Selection Sort")
print(SelectionSort([5,8,2,4,3,6,1,0]))

print("Insertion Sort")
print(InsertionSort([5,8,2,4,3,6,1,0]))

print("Merge Sort")
print(mergeSort([5,8,2,4,3,6,1,0]))