'''
Validate Sub sequence

Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

A sub sequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array but that are in the same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]. Not that a single number is an array and the array itself are both valid subsequences of the array.

Sample Input
array = [ 5, 1, 22, 5, 6, -1, 8, 10]
subsequence = [1, 6, -1, 10]

Sample Output 
true

Optimal Space & Time Complexity  
O(n) time complexity
O(1) space complexity
where, n is the length of the array   
'''
def bool2str(m_bool):
  if m_bool:
    return 'true'
  else:
    return 'false'
    
def isValidSubsequence(array, sequence):
    is_valid = False
    
    array = set(array)
    sequence = set(sequence)
    
    t = array.intersection(sequence)  
    if t == sequence:
      is_valid = True
    
    
    return bool2str(is_valid)
  
  
if __name__ == "__main__":
  array = [ 5, 1, 22, 5, 6, -1, 8, 10]
  subsequence = [1, 6, -1, 10]
  print(isValidSubsequence(array, subsequence))
  