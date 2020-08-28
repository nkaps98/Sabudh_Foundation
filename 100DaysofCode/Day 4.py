'''
Four Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
The function should find all quadruplets in the array that sum up to the largest sum and return a two dimensional array of all these
quadruplets in no particular order.

This is the last of its kind, I hope you would have understood the concept of storing complements in the set / dictionary or after sorting the list we can use two pointers to decide whether to decrement / increment the pointers. This problem also works on the similar principle, so don't get trapped into the 4 loop Naive Solution.

Sample Input

array = [7,6,4,-1,1,2]
targetSum = 16

Sample Output
// the quadruplets could be ordered differently
[[7, 6, 4, -1], [7, 6, 1, 2]]

Optimal Space & Time Complexity

Average: O(n^2) time | O(n^2) space - where n is the length of the input arrayTwo
Worst: O(n^3) time | O(n^2) space - where n is the length of the input array

'''
def fourNumberSum(array, targetSum):
  result = []
  array.sort()
  n = len(array)
  if len(array)<4:
    return []
  for i in range(n):
    for j in range(i+1,n):
      start = j+1
      end = n-1
      
      while start<end:
        temp_sum = array[i] + array[j] + array[start] + array[end]
        if temp_sum == targetSum:
          result.append(sorted([array[i], array[j], array[start], array[end]]))
          
          prev_s = array[start]
          while start<end and prev_s == array[start]:
            start+=1
          
          prev_e = array[end] 
          while start>end and prev_e == array[end]:
            end-=1
            
        elif temp_sum < targetSum:
          start+=1
        else:
          end-=1
  return result
if __name__ == "__main__":
  array = [7,6,4,-1,1,2]
  targetSum = 16
  output = fourNumberSum(array, targetSum)
  print(output)
  
