'''Two Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum upto the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array. 
Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum.You can assume that there will be at most one pair of numbers summing up to the target sum.

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
[-1, 11] // the numbers could be in reverse order
'''

def twoNumberSum(array, targetSum):
    """
      Input: array, targetSum
      Return: List of the two numbers whose sum is equal to the targetSum
    """
    tar_list = set()
    array = set(array)
    for item in array:
      sec_item = targetSum - item
      if sec_item in array and sec_item!=item:
        tar_list.add(item)
        tar_list.add(sec_item)
    
    
    return list(tar_list)

if __name__=='__main__':
  print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6],10))
