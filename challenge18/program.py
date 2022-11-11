import sys
import collections

Graph = collections.namedtuple('Graph', 'edges degrees')

def read_graph(num_lines):
    edges = collections.defaultdict(list)
    degrees = collections.defaultdict(int)
    for _ in range(int(num_lines)):
        line = sys.stdin.readline()
        res = line.strip().split(' ')
        target = res[0]
        sources = res[1:]
        for source in sources:
            edges[target].append(source)
            degrees[source] += 1
            degrees[target]
                
    return Graph(edges, degrees)

def topological_sort(graph):
    frontier = ['jailbreak']
    visited = set()
    
    while frontier:
        vertex = frontier.pop()
        visited.add(vertex)
        for neighbor in graph.edges[vertex]:
            if neighbor in visited:
                continue
            # else ...    
            frontier.append(neighbor)
            
    # to get num dependencies
    # len(visited) - 1
    return visited

def get_max_concurrency(graph, visited):
    
    # tuple (vertex, level)
    frontier = [(v,0) for v in graph.degrees if graph.degrees[v] == 0]
    level_dict = dict()
    while frontier:
        vertex, level = frontier.pop()
        if vertex in visited:
            level_dict[vertex] = level

        for neighbor in graph.edges[vertex]:
            graph.degrees[neighbor] -= 1
            if graph.degrees[neighbor] == 0: 
                frontier.append((neighbor, level + 1))
    
    # counts number of times each level occurs
    num_count = collections.Counter(list(level_dict.values()))
    
    # res = max of the counter
    return max(num_count.values())
      
def main():
    for line in sys.stdin:
        if int(line) == 0:
            break
        
        graph = read_graph(line)
        visited = topological_sort(graph)
        print(f"Number of Dependencies: {len(visited) - 1}")
        print(f"Maximum Concurrency: {get_max_concurrency(graph, visited)}") 

if __name__ == '__main__':
    main()