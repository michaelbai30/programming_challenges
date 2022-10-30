import sys
from collections import deque
global counter
counter = 0
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# create Binary Tree recursively given list of nodes
def create_BCT(nodes, index):
    if index >= len(nodes):
        return None
    
    root = Node(nodes[index]) 
    root.left = create_BCT(nodes, 2 * index + 1)
    root.right = create_BCT(nodes, 2 * index + 2) 

    return root

# helper function for recursive DFS
def helper(root, path, target):
    global counter
    if root is None:
        return
    
    path.append(root.val)
    if path[-len(target): ] == target:
    
            #print(f'curpath --- {path[-len(target):]}')
            #print('yes')

        counter += 1
    
    helper(root.left, path, target)
    helper(root.right, path, target)
    
    #print(f'path --- {path}')
   
    
    path.pop()
    
    
def dfs(root, target):
    global counter
    helper(root, [], target)
    
    return counter

def main():
    
   cases = []
   for line in sys.stdin:
       cases.append([int(x) for x in line.strip().split()]) 
       
   for case in cases:
        global counter
        binary = "{0:b}".format(case[0])
        binary_arr = [int(x) for x in str(binary)]
        nodes = [int(x) for x in str(case[1])]
        count = dfs(create_BCT(nodes, 0), binary_arr)
        print(f"Paths that form {case[0]} in binary ({binary}): {count}")
        counter = 0 
        
        
if __name__ == '__main__':
    main()
