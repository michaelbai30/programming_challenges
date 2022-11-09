import sys
import heapq
import math

def create_graph(coords):
    # adjacency list
    graph= {i:[] for i in range(len(coords))}
    
    for i in range(len(coords)):
        x1 = coords[i][0]
        y1 = coords[i][1]
        # for each other coordinate
        for j in range(i + 1, len(coords)):
            x2 = coords[j][0]
            y2 = coords[j][1]
            # calc pythagorean distance
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            
            # append to adjacency list both ways (because undirected)
            graph[i].append((distance, j))
            graph[j].append((distance, i))
    return graph

def MST(graph):
    visited = set()
    start = list(graph.keys())[0]
    frontier = [(0,start)]
    res = 0
    
    # Prim's MST algorithm
    while frontier:
        # priority queue
        distance, city = heapq.heappop(frontier)
       
        if city in visited:
            continue
        
        visited.add(city)

        res += distance
        
        for neighbor in graph[city]:
            if neighbor[1] not in visited:
                heapq.heappush(frontier, neighbor)
                
    return res

def main(): 
    case = []
    list_of_cases = []
    # read in test cases
    for line in sys.stdin:
        if int(line) == 0:
            break
        for _ in range(int(line)):
            one_line = sys.stdin.readline() 
            coords = [float(element) for element in one_line.strip().split(' ')]
            case.append(coords.copy())

        list_of_cases.append(case.copy())
        case.clear()
    
    # print res
    for case in list_of_cases:
        graph = create_graph(case)
        print(format(MST(graph), '.2f'))
        
if __name__ =='__main__':
    main()