# challenge 15 
import sys
import collections

def read_graph(num_edges):
    graph = collections.defaultdict(list)
    
    for _ in range(num_edges):
        source, target = map(int, sys.stdin.readline().split())
        graph[source].append(target)
        graph[target].append(source)
        
    return graph

def walk(graph, vertex, prev, visited, longest):
    longest = 0
   
    # if edge has already been visited 
    if (prev, vertex) in visited or (vertex, prev) in visited:
        return 0
    
    for neighbor in graph[vertex]:
        # add edge to visited    
        visited.add((vertex, prev))
        visited.add((prev,vertex))
        # if new edge
        longest = max(walk(graph, neighbor, vertex, visited, longest) + 1, longest)
        # called once the we pop out of the recursive call
        visited.remove((vertex,prev))
        visited.remove((prev,vertex)) 
    return longest     

def main():
    num_nodes, num_edges = map(int, sys.stdin.readline().split())
    while num_nodes and num_edges:
        
        max_longest = 0  
        graph = read_graph(num_edges)
        
        # iterate from each vertex in the graph
        # to get longest path
        for vertex in graph.keys():
            max_longest = max(max_longest, walk(graph, vertex, -1, set(), 0))
        
        # result
        print(max_longest - 1)
        
        num_nodes, num_edges = map(int, sys.stdin.readline().split())
    
if __name__ =='__main__':
    main()
