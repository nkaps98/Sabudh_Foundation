def threeNumberSum(array, targetSum):
    # Write your code here.
  triplet_list = []
  array.sort()
  set_array = set(array)
  for i in range(0,len(array)):
    set_array = set(array[i:])
    set_array.remove(array[i])
    for j in range(i+1,len(array)):
      set_array.remove(array[j])
      triplet = []
      item3 = targetSum-(array[i]+array[j])
      if item3 in set_array and array[i]!=array[j]!=item3:
        triplet.append(array[i])
        triplet.append(array[j])
        triplet.append(item3)
      if triplet!=[]:    
        triplet_list.append(triplet)
  
  return triplet_list
  
        
    
    
if __name__ == '__main__':
  array =  [12, 2, 1, 3, -6, 5, -8, 6]
  targetSum = 0
  print(threeNumberSum(array, targetSum))
  