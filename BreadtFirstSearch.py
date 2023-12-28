def breadth_first_search(graph, start_node, goals, traps):
    queue = [(start_node, [start_node], 0)]  # Kuyruk yapısı ve maliyet bilgisini ekleyin
    visited = set()  # Ziyaret edilen düğümleri tutan set
    expanded_nodes = []  # Genişletilen (expanded) düğümleri tutan liste
    total_cost = 0  # Toplam maliyet bilgisini tutacak değişken

    while queue:
        node, path, cost = queue.pop(0)  # Kuyruktan düğümü, yolunu ve maliyetini al
        visited.add(node)
        expanded_nodes.append(node)

        if tuple(map(int, node.split(','))) in goals:
            print("Goal node reached:", node)
            print("Solution Path:", path)
            total_cost = cost  # Eğer hedef düğüme ulaşıldıysa, toplam maliyeti güncelle
            break

        for neighbour in graph[node]:
            new_cost = cost
            if tuple(map(int, neighbour.split(','))) in traps:
                new_cost += 6  # Eğer komşu bir trap ise, +6 maliyet ekle
            else:
                new_cost += 1  # Değilse, +1 maliyet ekle

            if neighbour not in visited:
                queue.append((neighbour, path + [neighbour], new_cost))  # Yeni yol ve maliyet bilgisini ekle

    if total_cost:
        return expanded_nodes, total_cost  # Hedefe ulaşıldıysa genişletilmiş düğümleri ve toplam maliyeti döndür
    else:
        print("Goal nodes not found in the given graph.")
        return expanded_nodes, total_cost

# 'tree.txt' dosyasından veri okuma ve graph oluşturma
graph = {}

with open('maze.txt', 'r') as file:
    for line in file:
        line = line.strip()
        parts = line.split(':')
        key = parts[0].strip()
        values = parts[1].strip().split()
        graph[key] = values

print('Graph:', graph)

# Örnek kullanım
start_node = '3,2'  # Başlangıç düğümü
goals = {(3, 7), (6, 7), (8, 8), (8, 5), (7, 2)}
traps = {(2, 4), (3, 6), (5, 3), (6, 1), (7, 1), (7, 6), (7, 8), (4, 1), (4, 2)}
expanded_nodes, total_cost = breadth_first_search(graph, start_node, goals, traps)

print("Expanded Nodes:", expanded_nodes)
print("Total Cost:", total_cost)
