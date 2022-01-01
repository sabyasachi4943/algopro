# 1st way - with while loop
# O(n) time | O(1) space
def validateSubsequence(array, sequence):
  # initial the index at 0
  arrIdx = 0 
  seqIdx = 0
  # while the array index is less than length of array and the sequence index is less than sequence index
  while arrIdx < len(array) and seqIdx < len(sequence):
    # if we found our element we will move forward and increase sequence index by 1
    if array[arrIdx] == sequence[seqIdx]:
      seqIdx += 1
    # regardless we found any match or not we will move forward
    arrIdx += 1
  return seqIdx == len(sequence)

# 2nd way - with for loop
# O(n) time | O(1) space
def validateSubsequence(array, sequence):
  seqIdx = 0
  for value in array:
    if seqIdx == len(sequence):
      break
    if sequence[seqIdx] == value:
      seqIdx += 1
  return seqIdx == len(sequence)