import sys
import collections

def read_graph(n, m):
    g = collections.defaultdict(list)
    
    for _ in range(m):
        source, target = map(int, sys.stdin.readline().split())
        g[source].append(target)
        g[target].append(source)
        
    return g

def walk(g, v, prev, visited, longest):
    longest = 0
   
    # if edge has already been visited 
    if (prev, v) in visited or (v, prev) in visited:
        return 0
    
    for neighbor in g[v]:
        # add edge to visited    
        visited.add((v, prev))
        visited.add((prev,v))
        # if new edge
        longest = max(walk(g, neighbor, v, visited, longest) + 1, longest)
        # called once the we pop out of the recursive call
        visited.remove((v,prev))
        visited.remove((prev,v)) 
    return longest     

def main():
    n, m = map(int, sys.stdin.readline().split())
    while n and m:
        
        max_longest = 0  
        g = read_graph(n, m)
        
        # iterate from each vertex in the graph
        # to get longest path
        for v in g.keys():
            max_longest = max(max_longest, walk(g, v, -1, set(), 0))
        
        # result
        print(max_longest - 1)
        
        n, m = map(int, sys.stdin.readline().split())
    
if __name__ =='__main__':
    main()