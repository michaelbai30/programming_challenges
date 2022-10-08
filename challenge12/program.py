# Note: My solution takes heavy inspiration from Bui's "Hunting Squirrels" solution
import sys

def read_grid(n):
    grid = [[0 for _ in range(n + 1)]]      # Pad grid
    # create a n + 1 by n + 1 grid from user entered values.
    # We will use indices 1 to n + 1.
    for _ in range(n):
        grid.append([0] + list(map(int, sys.stdin.readline().split())))
    return grid

def min_kakamora(grid, n):
    table = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]
    
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            # update table based on the value of the square + min(up, left, up-left)
            table[r][c] = min(table[r-1][c], table[r][c-1], table[r-1][c-1]) + grid[r][c]
            table[1][1] = grid[1][1]
            
    return table

def find_path(grid, n, table):
    path = []
    r, c = n, n 
    while r > 0 and c > 0:
        path.append(grid[r][c])
        
        # backtrack left
        if table[r][c] - grid[r][c] == table[r][c - 1]:
            c -= 1
        # backtrack up
        elif table[r][c] - grid[r][c] == table[r - 1][c]:
            r -= 1
        # backtrack up-left
        else:
            r -= 1
            c -= 1
    path.reverse()
    
    return path

def main():
    while True:
       
       try: 
            n = int(sys.stdin.readline())
            # signifies end of input
            if n == 0:
                break
       except ValueError:
           break
       
       grid = read_grid(n)
       table = min_kakamora(grid, n)
       path = find_path(grid, n, table)
       
       print(table[n][n])
       print(' '.join(str(c) for c in path))
    
if __name__ == '__main__':
    main()