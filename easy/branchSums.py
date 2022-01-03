class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


# O(n) time | O(n) space
def branchSums(root):
  sums = []
  calculateBranchSums(root, 0, sums)
  return sums

def calculateBranchSums(node, runningSum, sums):
  if node is None:
    return

  newRunnningSum = runningSum + node.value
  if node.left is None and node.right is None:
    sums.append(newRunnningSum)
    return

  calculateBranchSums(node.left, newRunnningSum, sums)
  calculateBranchSums(node.right, newRunnningSum, sums)