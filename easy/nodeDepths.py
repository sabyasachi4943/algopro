# 1st method - itteratively
# O(n) time | O(h) space
def nodeDepths(root):
  sumOfDepths = 0
  stack = [{"node": root, "depth": 0}]
  while len(stack) > 0:
    nodeInfo = stack.pop()
    node, depth = nodeInfo["node"], nodeInfo["depth"]
    if node is None:
      continue
    sumOfDepths += depth
    stack.append({"node": node.left, "depth": depth +1})
    stack.append({"node": node.right, "depth": depth + 1})
  return sumOfDepths

# 2nd method - recurrsive method
# O(n) time | O(h) space
def nodeDepths(root, depth = 0):
  if root is None:
    return 0
  return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)
