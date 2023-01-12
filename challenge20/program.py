from collections import defaultdict
import sys

def read_graph(stream=sys.stdin):
    n = int(stream.readline())
    if not n:
        return None, None, None
    source, target, connections = map(int, stream.readline().split())
    graph = defaultdict(lambda: defaultdict(int))
    
    for _ in range(connections):
        s, t, w = map(int, sys.stdin.readline().split())
        graph[s][t] += w
        graph[t][s] += w
    return source, target, graph

def find_flow(source, target, graph):
    frontier = [(source, -1)] # (cur, prev)
    visited = {} # {node : prev}
    
    while frontier:
        # remove a node using BFS (queue)
        node, prev = frontier.pop(0)
    
        if node in visited:
            continue
        
        # mark visited[node] = prev
        visited[node] = prev
        
        # check if node is target (sink) -> return visited 
        if node == target:
            return visited 
         
        # for each neighbor:
            # add neighbor if capacity > 0
        for neighbor in graph[node]:
            if graph[node][neighbor] > 0:
                frontier.append((neighbor, node))
                 
    return {} 
        
def compute_min_flow_path(visited, start, target, graph):
    #use visited to walk backwards from target
    # -> keep track of minimum edge weight
    # return minimum edge weight
    min_edge_weight = sys.maxsize
    cur = target
    while start != cur:
        source = visited[cur]
        min_edge_weight = min(graph[cur][source], min_edge_weight)
        cur = source
    return min_edge_weight

# backtrack and subtract helper
def subtract_weights(visited, start, target, graph, weight):
    cur = target
    while start != cur:
        source = visited[cur]
        # bidirectionality
        graph[source][cur] -= weight
        graph[cur][source] -= weight
        cur = source

def main():
    case = 0
    while True:    
        bandwidth = 0
        case += 1
        source, target, graph = read_graph()
        if not source or not target:
            break
        
        # go through path and subtract weights
        # repeat until path is empty 
        while True:    
            path = find_flow(source, target, graph)
            if not path:
                break
            weight = compute_min_flow_path(path, source, target, graph)
            # backtrack and subtract weight given 
            subtract_weights(path, source, target, graph, weight)
            bandwidth += weight
        
        print(f'Network {case}: Bandwidth is {bandwidth}.')
        
if __name__ == '__main__':
    main()       
