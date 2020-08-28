'''
Move Element to End

You're given an array of integers and an integer. Write a function that moves all instance of that integer in the array to the end of the array and returns the array.

Write a function that should perform this in place (i.e , it should mutate the input array) and doesn't need too maintain the order of the other integer.

Sample Input;

array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

Sample Output:

[1, 3, 4, 2, 2,2,2,2] // the number 1, 3, and 4 could be ordered differently
Time Complexity:

O(n) time | O(1) space,
where n, is the length of the array
'''
def moveElementToEnd(array, toMove):
    # Write your code here.
    array.sort()
    start = 0
    pos = 0
    for i in range(0,len(array)):
      prev = array[i-1]
      
      if array[i] == toMove and prev!=toMove:
        pos = i
        start+=1
      elif array[i] == toMove and prev==toMove:
        start+=1
      elif array[i] > prev and prev==toMove:
        temp = array[pos]
        array[pos] = array[i]
        array[i] = temp
        pos+=1
    return array
        

if __name__ == "__main__":
  array = [2, 1, 2, 2, 2, 3, 4, 2]
  toMove = 2
  print(moveElementToEnd(array, toMove))
  
  # for i in range(0,len(array)):
  #     print(array,t)
  #     prev = array[start]
  #     if array[i] == toMove and prev!=toMove:
  #       t = i
  #       start+=1
  #     elif array[i] == toMove and prev==toMove:
  #       start+=1
  #     elif array[t] <= array[i] and array[t]==toMove and prev<array[i]:
  #       print(array[i],array[t],t)
  #       temp = array[t]
  #       array[t] = array[i]
  #       array[i] = temp
  #       t+=1
  #   return array
