from collections import defaultdict
import sys

def read_graph():
    graph = defaultdict(list)
    for line in sys.stdin:
        if line.split() == ['%']:
            break
        source, target = map(int, line.split())
        graph[source].append(target)
        graph[target].append(source)
        
    return graph

def find_cycle(graph, start, vertex, visited, path, num_nodes):
    
    # base case
    # path is the expected length
    # and the last vertex is equal to the first vertex 
    if len(path) == num_nodes:
            return path if start in graph[vertex] else []
    
    for neighbor in sorted(graph[vertex]): 
        if neighbor in visited:
            continue
        path.append(neighbor)
        visited.add(neighbor)
        # recursive step - call on neighbor
        if find_cycle(graph, start, neighbor, visited, path, num_nodes):
            return path
         
        path.pop()
        
        visited.remove(neighbor)
        
    return []

def main():
    for line in sys.stdin:
        graph = read_graph()
        num_nodes = int(line)
        the_set = set()
        the_set.add(1)
        # start and neighbor always at 1
        path = find_cycle(graph, 1, 1, the_set, [1], num_nodes)
        if path:
            path.append(1)
            print(' '.join(map(str, path)))
        else:
            print('None')

if __name__ == '__main__':
    main() 
