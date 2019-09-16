#creating find the repeating char

def NaiveApproach(arr):
  # O(nxm)
    newarr = []
    for i in arr: #O(n)
        if i in newarr: #O(n)
            return i
        newarr.append(i)
    return False

def AnotherNaiveAppraoch(arr):
  #If we do a binary search on this wed get alittle better than O(nxm)
  # this returns 2 for [2,5,5,2] while the other returns 5
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                return arr[j]
    return False


def FindRep(arr):
    if len(arr)<2:
        return False
    valDict = {}
    print("here")
    for i in range(len(arr)):
        try:
          if valDict[arr[i]]:
              return arr[i]          
        except:
          valDict[arr[i]]= arr[i]
          
    return False

print(AnotherNaiveAppraoch([2,5,5,2]))