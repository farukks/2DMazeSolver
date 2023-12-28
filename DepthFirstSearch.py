def depth_first_search(root_node, graph, goals, traps):
    stack = [root_node]
    visited = set()  # Ziyaret edilen düğümleri tutmak için set oluşturuldu
    visited_array = []
    solution_path = []
    cost = 0  # Toplam maliyet
    while stack:
        node = stack.pop(0)
        if node not in visited:
            visited.add(node)  # Düğümü ziyaret edildi olarak işaretle
            stack = graph[node] + stack
            visited_array.append(node)
            print(f"Visited Node: {node}")
            solution_path.append(node)
            last_node = solution_path[-1]
            
            # Trap kontrolü
            if tuple(map(int, node.split(','))) in traps:
                cost += 6
            else:
                cost += 1
            
            if last_node in graph:
                values = graph[last_node]
                print("Yeni ziyaret edilen değerin valuesları ", values)
                set1 = set(values)
                set2 = set(visited_array)
                set3 = set(goals)
                print(f"{values} anahtarının değerleri:")
                intersection = set1.intersection(set3)
    
                if set1.issubset(set2):
                    print("Values'ların hepsi ziyaret edilmiş.")
                    last_node = (last_node)
                    print("Last node değeri :", last_node)
                    print("Goals değerleri : ", goals)
                    if set(last_node) in goals:
                        print(f"{last_node} değeri goals içinde, çıkarılmadı.")
                    else:
                        print(f"{last_node} değeri goals içinde değil, çıkarıldı.")
                        solution_path.remove(last_node)
                          
                else:
                    print("Values'ların hepsi ziyaret edilmemiş.")
            
            # Hedef düğümleri kontrol et
            if tuple(map(int, node.split(','))) in goals:
                print(f"Goal node reached: {node}")
                print("Solution path goals içinde : ", solution_path)
                return visited_array, cost  # Hedefe ulaşıldığında fonksiyonu sonlandır ve ziyaret edilen yolu ve maliyeti döndür
            print("Solution path : ", solution_path)
    return visited_array, cost  # Hedefe ulaşılmadığında ziyaret edilen yolu ve maliyeti döndür

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
node = '3,2'  # Başlangıç düğümü
goals = {(3, 7), (6, 7), (8, 8), (8, 5), (7, 2)}
traps = {(2, 4), (3, 6), (5, 3), (6, 1), (7, 1), (7, 6), (7, 8), (4, 1), (4, 2)}
component, total_cost = depth_first_search(node, graph, goals, traps)
print('DFS Path:', component)
print(f"Following is the Depth-first search: {component}")
print(f"Total Cost: {total_cost}")
