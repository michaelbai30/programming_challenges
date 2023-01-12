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
    
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            # update table based on the value of the square + min(up, left, up-left)
            table[row][col] = grid[row][col] + min(table[row-1][col], 
                                                    table[row][col-1], 
                                                    table[row-1][col-1])
            table[1][1] = grid[1][1]
            
    return table

def find_path(grid, n, table):
    path = []
    row, col = n, n 
    while row > 0 and col > 0:
        path.append(grid[row][col])
        
        # backtrack left
        if table[row][col] - grid[row][col] == table[row][col - 1]:
            col -= 1
        # backtrack up
        elif table[row][col] - grid[row][col] == table[row - 1][col]:
            row -= 1
        # backtrack up-left
        else:
            row -= 1
            col -= 1
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
        print(' '.join(str(element) for element in path))
    
if __name__ == '__main__':
    main()
