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


def depth_limited_search(graph, start, goal, depth, traps, cost_so_far):
    if depth == 0 and start in goal:
        return cost_so_far, [start], {start}  # Cost, Path, Expanded Nodes
    if depth > 0:
        expanded_nodes = {start}
        min_cost = float('inf')
        best_path = []
        best_expanded_nodes = set()

        for neighbor in graph.get(start, []):
            trap_cost = 6 if neighbor in traps else 1
            next_cost = cost_so_far + trap_cost

            # Tuzaktan geçme koşulunu kontrol et
            if trap_cost > 1 and next_cost > cost_so_far + 6:
                continue

            sub_cost, sub_path, sub_nodes = depth_limited_search(graph, neighbor, goal, depth - 1, traps, next_cost)
            expanded_nodes = expanded_nodes.union(sub_nodes)  # Başarısız yolları da dahil et
            if sub_cost < min_cost:
                min_cost = sub_cost
                best_path = [start] + sub_path
                best_expanded_nodes = expanded_nodes

        if min_cost != float('inf'):
            return min_cost, best_path, best_expanded_nodes
        return float('inf'), [], expanded_nodes
    return float('inf'), [], {start}

# Diğer fonksiyonlar ve kodlar aynı kalacak

# İteratif derinleşme araması fonksiyonu
def iterative_deepening_search(graph, start, goals, traps):
    for depth in range(len(graph)):
        cost, path, expanded_nodes = depth_limited_search(graph, start, goals, depth, traps, 0)
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
