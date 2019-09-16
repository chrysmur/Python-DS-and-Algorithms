

def testIntersectionOn(array1, array2):
    if set(array1).intersection(set(array2)):
        return True
    return False

def testIntersectionOn2(array1, array2):
    for val in array1:
        for val2 in array2:
            if val==val2:
                return True
    return False

def testIntersectionOn1(array1, array2):
    array1_dict = {i:True for i in set(array1)}
    for val in array2:
      try:
        if array1_dict[val]:
            return True
        return False
      except:
        pass

print("Big O(len(array1)+len(array2)==> Linear")
print(testIntersectionOn([1,2,3],[4,2,6]))
print("Big O(len(array1)*len(array2)==> Quadratic")
print(testIntersectionOn2([1,2,3],[4,2,6]))
print("Another Big O(len(array1)+len(array2)==> Linear")
print(testIntersectionOn1([1,2,3],[4,2,6]))