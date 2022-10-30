import sys
global COUNTER
COUNTER = 0

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# create Binary Tree recursively given list of nodes
def create_bct(nodes, index):
    if index >= len(nodes):
        return None
    
    root = Node(nodes[index])
    root.left = create_bct(nodes, 2 * index + 1)
    root.right = create_bct(nodes, 2 * index + 2) 

    return root

# helper function for recursive DFS
def helper(root, path, target):
    global COUNTER
    if root is None:
        return
    
    path.append(root.val)
    helper(root.left, path, target)
    helper(root.right, path, target)
    
    # counts the last N elements of path and compares to target
    if path[-len(target): ] == target: 
        COUNTER += 1
        
    if path: 
        path.pop()
    
def dfs(root, target):
    global COUNTER
    helper(root, [], target)
    
    return COUNTER

def main():
    cases = []
    for line in sys.stdin:
        cases.append(line.strip().split())
       
    for case in cases:
        global COUNTER
        binary = "{0:b}".format(int(case[0]))
        binary_arr = [int(x) for x in str(binary)]
        nodes = [int(x) for x in case[1]]
        count = dfs(create_bct(nodes, 0), binary_arr)
        print(f"Paths that form {case[0]} in binary ({binary}): {count}")
        # reset counter after each case
        COUNTER = 0 

if __name__ == '__main__':
    main()