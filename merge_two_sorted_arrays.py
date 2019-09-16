def mergeAndSorted(arr1,arr2):
    merged = arr1 + arr2
    print("Before Sorting", merged)
    sortedA = []
    for i in range(len(merged)):
        mini =min(merged) 
        sortedA.append(mini)
        merged.remove(mini) #O(n)
    print("After Sorting", sortedA)
    #Bad O(n^2)


def mergeSorted(arr1,arr2):
    '''assume that they are sorted'''
    if len(arr1)==0:
      return arr2
    if len(arr2)==0:
      return arr1
    merged =[]
    i=0
    j = 0
    if len(arr1) < len(arr2):
        minarr = arr1
        maxarr = arr2
    else:   
        minarr = arr2
        maxarr = arr1
    for num in range(len(minarr)+1):
        print(i,j)
        if arr1[i]< arr2[j]:
            merged.append(arr1[i])
            if i == len(arr1)-1:
                merged.append(arr1[j])
                j+=1
            i+=1
        elif arr2[j]< arr1[i]:
            merged.append(arr2[j])
            if j == len(arr2)-1:
                merged.append(arr1[i])
                i+=1
            j+=1
        elif arr2[j] == arr1[i]:
            merged.append(arr2[j])
            merged.append(arr1[i])
            i+=1
            j+=1
    merged = merged + maxarr[len(minarr):]
    print(merged)
    
    
one = [4,5,7,8] 
two = [1,4,6]
mergeSorted(one,two)