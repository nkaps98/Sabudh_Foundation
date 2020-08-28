'''
Smallest Difference   
Write a function that takes in two non-empty arrays of integers, find the pair of numbers (one from each array) whose absolute difference is closet to zero, and returns an array containing these two numbers, with the numbsers, with the number from the first array in the first position.

You can assume that there will only be one pair of numbers with the smallest difference.

Sample Input

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

Sample Output

[28, 26]
'''
def smallestDifference(arrayOne, arrayTwo):
  
  '''
  Input: arrayOne, arrayTwo
  Result: Returns pair of numbers with difference closest to 0
  '''
  arrayOne = sorted(arrayOne)
  arrayTwo = sorted(arrayTwo)
  
  small = arrayTwo[len(arrayTwo)-1]
  for i in range(0, len(arrayOne)):
    low = 0
    high = len(arrayTwo)-1
    while low<=high:
      middle = int((low + high)/2)
      diff_mid = arrayOne[i]-arrayTwo[middle]
      
      abs_value = abs(0 - diff_mid)
      
      if abs_value < small:
        small = abs_value
        pair = [arrayOne[i],arrayTwo[middle]]
      
      if diff_mid < 0:
        high = middle - 1
      else:
        low = middle + 1
  return pair

if __name__ == "__main__":
  arrayOne = [-1, 5, 10, 20, 28, 3]
  arrayTwo = [26, 134, 135, 15, 17]
  print(smallestDifference(arrayOne, arrayTwo))