import sys
from collections import deque

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# leverage the fact that the array is sorted 
# by using the median num to determine 
# which nodes go to the left or right of root.
def create_BST(nums):
    length = len(nums)
    
    # base case: return when empty
    if length == 0:
        return None

    median = length // 2
    
    root = Node(nums[median])
    
    # call createBST with array values to the left of median
    root.left = create_BST(nums[0 : median])
    
    # to the right of median
    root.right = create_BST(nums[median + 1 : ])
    
    return root

# BFS can be used to print in level order
def print_BFS(root):
    queue = deque([root])
    res = []
    
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            if level and level not in res:
                # store levels in a list
                res.append(level)
    
    for level in res:
        print(' '.join(str(e) for e in level))
        
def main():
    cases = []
    for line in sys.stdin:
        cases.append([int(x) for x in line.strip().split()]) 
    for case in cases:
        print_BFS(create_BST(case))
        
if __name__ == '__main__':
    main()