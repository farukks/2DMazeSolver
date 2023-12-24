import heapq
import math


def maze(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip().split(':')
            node = tuple(map(int, line[0].split(',')))
            neighbors = [tuple(map(int, neighbor.split(','))) for neighbor in line[1].split()]
            graph[node] = neighbors
    return graph


def heuristic(node, goals):
    # Using Euclidean distance as the heuristic
    return min(math.sqrt((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2) for goal in goals)


def a_star_search(graph, start, goals, traps):
    visited = set()
    expanded_nodes = set()
    priority_queue = [(heuristic(start, goals), 0, start, [])]  # f(n), g(n), node, path
    while priority_queue:
        f, cost, node, path = heapq.heappop(priority_queue)
        if node in visited:
            continue
        visited.add(node)
        expanded_nodes.add(node)

        if node in traps:
            cost += 6  # Additional cost for traps

        if node in goals:
            return cost, path + [node], expanded_nodes  # Return cost, path, and expanded nodes

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                new_cost = cost + 1  # Assuming each step has a cost of 1
                f = new_cost + heuristic(neighbor, goals)  # f(n) = g(n) + h(n)
                heapq.heappush(priority_queue, (f, new_cost, neighbor, path + [node]))
    return float('inf'), [], expanded_nodes  # If none of the goals is reachable


traps = {(2, 4), (3, 6), (5, 3), (6, 1), (7, 1), (7, 6), (7, 8), (4, 1), (4, 2)}
goals = {(3, 7), (6, 7), (8, 8), (8, 5), (7, 2)}
goal = {"G1": (3, 7),
        "G2": (6, 7),
        "G3": (8, 8),
        "G4": (8, 5),
        "G5": (7, 2)
        }


file_path = 'C:/newFile.txt'
graph = maze(file_path)

cost, path, expanded_nodes = a_star_search(graph, (3, 2), goals, traps)
state = path[-1]  # Get the last element of the path
goal_state = [key for key, value in goal.items() if value == state]
if cost < float('inf'):
    print("Goal state found :", goal_state[0], state)
    print("Cost to reach the goal:", cost)
    print("Path to the goal:", path)
    print("Expanded nodes:", expanded_nodes)
else:
    print("None of the goals is reachable from the starting point.")
