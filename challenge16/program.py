import sys
import collections
import heapq

# from stdin: create a 2D array grid
def read_grid(n):
    col = []
    row = []
    for _ in range(n):
        line = sys.stdin.readline().split()
        for element in line:
            col.append(element)
        row.append(col)
        col = []
    return row

# from 2D array, create graph with valid neighbors + weight
def read_graph(grid):
    graph = collections.defaultdict(dict)
    # we can move to cells of value 'S', '0', or 'E', avoiding '1'
    valid_moves = {'S', '0', 'E'}
    row_sz = len(grid)
    col_sz = len(grid[0])
    for i in range(row_sz):
        for j in range(col_sz):
            cell_id = i * col_sz + j
            if grid[i][j] in valid_moves:
                # up - left
                # if index for up - left in bounds and the value is a valid move ... 
                if (i - 1) >= 0 and (j - 1) >= 0 and grid[i - 1][ j - 1] in valid_moves:
                    # diag movements are weighted 2
                    graph[cell_id][((i - 1) * col_sz  + (j- 1))] = 2
                # up
                if (i - 1) >= 0 and grid[i - 1][j] in valid_moves: 
                    # ordinal movements are weighted 1
                    graph[cell_id][(i - 1) * col_sz  + (j)] = 1
                # up - right    
                if (i - 1) >= 0 and (j + 1) < col_sz and grid[i - 1][ j + 1] in valid_moves: 
                    graph[cell_id][((i - 1) * col_sz  + (j + 1))] = 2  
                # left     
                if (j - 1) >= 0 and grid[i][j - 1] in valid_moves: 
                    graph[cell_id][((i) * col_sz  + (j - 1))] = 1
                # right    
                if (j + 1) < col_sz and grid[i][ j + 1] in valid_moves: 
                    graph[cell_id][((i) * col_sz  + (j + 1))] = 1
                # down
                if (i + 1) < row_sz and grid[i + 1][j] in valid_moves: 
                    graph[cell_id][((i + 1) * col_sz  + (j))] = 1
                # down - left    
                if (i + 1) < row_sz and (j - 1) >= 0 and grid[i + 1][ j - 1] in valid_moves: 
                    graph[cell_id][((i + 1) * col_sz  + (j - 1))] = 2
                # down - right    
                if (i + 1) < row_sz and (j + 1) < len(grid[i]) and grid[i + 1][ j + 1] in valid_moves: 
                    graph[cell_id][((i + 1) * col_sz  + (j + 1))] = 2
    
    return graph

# Djikstra's 
def compute(graph, start):
    frontier = []
    visited = {}
    
    heapq.heappush(frontier, (0, start, start))
    while frontier:
        distance, target, source = heapq.heappop(frontier)
        
        if target in visited:
            continue
        visited[target] = source
        
        for neighbor, weight in graph[target].items():
           heapq.heappush(frontier, (weight + distance, neighbor, target))
            
        
    return visited       
    
def reconstruct(graph, visited, source, target):
    
    path = []
    cost = 0
    cur = target
 
    while cur != source:
        if cur not in visited:
            return None, 0
        if visited[cur] not in graph:
            return None, 0
        cost += graph[visited[cur]][cur]
        path.append(cur)
        cur = visited[cur]
        
    path.append(source)
    return reversed(path), cost

def main():
    n, m = map(int, sys.stdin.readline().split())
    
    while n and m:
        
        min_path= []
        min_cost = float('inf')
        grid = read_grid(n)
        graph = read_graph(grid)
        row_sz = len(grid)
        col_sz = len(grid[0])
        # search grid to get 'S' ID
        for i in range(row_sz):
            for j in range(col_sz):
                if grid[i][j] == 'S':
                    start_id =  i * col_sz + j
                    visited = compute(graph, start_id)
        for i in range(row_sz):
            for j in range(col_sz):
                # get 'E' ID
                if grid[i][j] == 'E':
                    end_id =  i * col_sz + j
                    path, cost = reconstruct(graph, visited, start_id, end_id)
                    # if path to current 'E' not found, continue. 
                    # there still may be another path to another 'E'
                    if path == None and cost == 0:
                        continue
                    elif cost < min_cost:
                        min_cost = cost
                        min_path = path
        if min_path:
            min_path = ' '.join(str(x) for x in min_path)
        else:
            min_cost = 0
            min_path = None
        
        print(f'Cost: {min_cost} Path: {min_path}')
        
        n, m = map(int, sys.stdin.readline().split())
        
if __name__ == '__main__':
    main()
