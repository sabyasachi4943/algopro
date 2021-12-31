
# first way - two for loops
# O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
    # all the way the before the last num/val of array
    for i in range(len(array) - 1):
        firstNum = array[i]
        # iterating through all the rest of the numbers in the array
        for j in range(i+1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
# if nothing is there return empty array
    return []


# second way - using hash tables
# 0(n) time | O(n) space
def twoNumberSum(array, targetSum):
    nums = {}
    # iterating the array
    for num in array:
        potentialMatch = targetSum - num
        # if the number is in the hash table then return the potentialMatch and the number
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            # just putting the number into the hash table
            nums[num] = True
    # if nothing is there return empty array
    return []


# third way - first sort the array
# O(nlog(n)) time | O(1) space
def twoNumberSum(array, targetSum):
    # sorting the array
    array.sort()
    # setting the left pointer
    left = 0
    # setting the right pointer to the last val of the array
    right = len(array) - 1
    # while two pointers don't overlap or while the left pointer do not pass the right pointer
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        # if the currentSum is less, then we want to increase the sum for greater val thus increasing the left pointer
        elif currentSum < targetSum:
            left += 1
        # if the currentSum is more, then we want to decrease the sum for lesser val thus decreasing the right pointer
        elif currentSum > targetSum:
            right -= 1
        # if nothing is there return empty array
    return []
