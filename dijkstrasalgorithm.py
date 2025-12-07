#daykstır

def dijkstra(graph: dict[str, dict[str ,float]] , start_point: str ) -> dict[str , float]:
    """
    Dijkstra'nın en kısa yol algoritmasını kullanarak, bir graph'taki düğümler 
    arasındaki en kısa yolları bulmayı sağlar.

    Args:
        graph (dict[str, dict[str, int]]): 
            Her bir düğüm, komşu düğümleri ve bu düğümlere olan 
            mesafeleri bir iç sözlük olarak tutar. 
            Örnek: 
            {
                'A': {'B': 4, 'C': 8},
                'B': {'A': 4, 'C': 6},
            }
        start_point (str): 
            Algoritmanın başlayacağı düğümün adı.

    Returns:
        dict[str, float]: 
            Başlangıç düğümünden her bir düğüme olan en kısa mesafelerin sözlüğü. 
            Ulaşılabilir olmayan düğümler için değer `float('inf')` olur.

    Example:
        graph = {
            'A': {'B': 3, 'C': 6, 'D': 4},
            'B': {'A': 3, 'C': 2, 'E': 3},
            'C': {'A': 6, 'B': 2, 'D': 2, 'E': 2, 'F': 3},
            'D': {'A': 4, 'C': 2, 'F': 5, 'G': 7},
            'E': {'B': 3, 'C': 2, 'F': 1},
            'F': {'C': 3, 'D': 5, 'E': 1, 'G': 1},
            'G': {'D': 7, 'F': 1}
        }
        start_node = 'A'
        shortest_distance = dijkstra(graph, start_node)
        #output: {'A': 0, 'B': 3, 'C': 5, 'D': 4, 'E': 6, 'F': 7, 'G': 8}
    """
    unvisited_node: list[str] = list(graph.keys())
    print(unvisited_node)
    updated_distance: dict[str , float] = { node : float('inf')  for node in graph }
    updated_distance[start_point] = 0

    while unvisited_node:
        
        current_node_n : str = min(unvisited_node , key = lambda node: updated_distance[node])

        if updated_distance[current_node_n ]== float('inf'):
            break

        for neighboor, weight in graph[current_node_n].items():
            new_distance : float = updated_distance[current_node_n] + weight
            
            if new_distance < updated_distance[neighboor]:
                updated_distance[neighboor] = new_distance
            
            print(f"current_node_N={current_node_n},   neighboor={neighboor},   weight={weight},  new_distance={new_distance}")
        
        print(updated_distance)
        unvisited_node.remove(current_node_n)

    return updated_distance
            
graph :dict[str, dict[str ,float]]= {
    'A': {'B': 3, 'C': 6, 'D': 4},
    'B': {'A': 3, 'C': 2, 'E': 3},
    'C': {'A': 6, 'B': 2, 'D': 2, 'E': 2, 'F': 3},
    'D': {'A': 4, 'C': 2, 'F': 5, 'G': 7},
    'E': {'B': 3, 'C': 2, 'F': 1},
    'F': {'C': 3, 'D': 5, 'E': 1, 'G': 1},
    'G': {'D': 7, 'F': 1}
}
start_node : str = 'G'

shortest_distance : dict[str , float]= dijkstra(graph, start_node)
#print(shortest_distance)

print(f"Starting node: {start_node}")
for node, distance in shortest_distance.items():
    print(f"Shortest distance to {node}: {distance}")
    
