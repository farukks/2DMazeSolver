import heapq
import math

# Labirenti yükleyip, graf olarak döndüren fonksiyon
def maze(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip().split(':')
            node = tuple(map(int, line[0].split(',')))
            neighbors = [tuple(map(int, neighbor.split(','))) for neighbor in line[1].split()]
            graph[node] = neighbors
    return graph


# Derinlik sınırlı arama fonksiyonu
def depth_limited_search(graph, start, goal, depth, traps):
    if depth == 0 and start in goal:
        return 0, [start], {start}  # Cost, Path, Expanded Nodes
    if depth > 0:
        expanded_nodes = {start}
        for neighbor in graph.get(start, []):
            if neighbor in traps:
                continue  # Skip traps in depth-limited search
            cost, path, nodes = depth_limited_search(graph, neighbor, goal, depth - 1, traps)
            if cost != float('inf'):
                return cost + 1, [start] + path, expanded_nodes.union(nodes)
        return float('inf'), [], expanded_nodes
    return float('inf'), [], {start}

# İteratif derinleşme araması fonksiyonu
def iterative_deepening_search(graph, start, goals, traps):
    for depth in range(len(graph)):
        cost, path, expanded_nodes = depth_limited_search(graph, start, goals, depth, traps)
        if cost != float('inf'):
            return cost, path, expanded_nodes
    return float('inf'), [], set()

# Example usage


# Labirent, tuzaklar ve hedefleri tanımlayın
traps = {(2, 4), (3, 6), (5, 3), (6, 1), (7, 1), (7, 6), (7, 8), (4, 1), (4, 2)}
goals = {(3, 7), (6, 7), (8, 8), (8, 5), (7, 2)}
goal = {"G1": (3, 7),
        "G2": (6, 7),
        "G3": (8, 8),
        "G4": (8, 5),
        "G5": (7, 2)
        }
# Labirenti yükleyin ve aramayı başlatın
file_path = 'maze.txt'
graph = maze(file_path)
cost, path, expanded_nodes = iterative_deepening_search(graph, (3, 2), goals, traps)
state = path[-1]  # Get the last element of the path
goal_state = [key for key, value in goal.items() if value == state]
if cost < float('inf'):
    print("Goal state found :", goal_state[0], state)
    print("Cost to reach the goal:", cost)
    print("Path to the goal:", path)
    print("Expanded nodes:", expanded_nodes)
else:
    print("None of the goals is reachable from the starting point.")
