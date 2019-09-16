 def pairsWithoutRep(array):
  #len(array)C2--> Order Does not Matter ba = ab is not ba
  for i in array:
    for j in array[array.index(i):]:
      if i != j:
        print(i,j)

def pairsWithRep(array):
  #len(array)P2 --> Order Matters ab != ba
  for i in array:
    for j in array:
      if i != j:
        print(i,j)

array = ['a','b','c','d','e','f']
print("Combinations")
pairsWithoutRep(array)
print("Permuation")
pairsWithRep(array)

print("Big O is: O(n*n)= O(n^2) or the Quadratic Time")