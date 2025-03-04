import time

def main_menu():
    while True:
        print("\n===== MENU CHALLENGES =====")
        print("1. Challenge 1")
        print("2. Challenge 2")
        print("3. Challenge 3")
        print("4. Keluar")
        
        choice = input("Pilih challenge (1-4): ")
        if choice == '1':
            challenge_1()
        elif choice == '2':
            challenge_2()
        elif choice == '3':
            challenge_3()
        elif choice == '4':
            print("Terima kasih! Keluar...")
            break
        else:
            print("Pilihan tidak valid, coba lagi!")

def challenge_1():
    graph = {'A': ['B', 'C'], 'B': ['A', 'C', 'D'], 'C': ['A', 'B', 'D'], 'D': ['B', 'C']}
    print("\n===== Challenge 1 =====")
    start_time = time.time()
    print("Trail dari A ke D:", find_all_paths(graph, 'A', 'D'))
    print("Semua Path dari A ke D:", find_all_paths(graph, 'A', 'D'))
    print("Semua Cycle yang melewati A:", find_all_cycles(graph, 'A'))
    print(f"Waktu eksekusi: {time.time() - start_time:.4f} detik")
    kembali_ke_menu()

def challenge_2():
    graph = {'A': ['B', 'D'], 'B': ['A', 'C', 'E'], 'C': ['B', 'F'], 'D': ['A', 'E'], 'E': ['B', 'D', 'F'], 'F': ['C', 'E']}
    print("\n===== Challenge 2 =====")
    start_time = time.time()
    print("Semua Path dari A ke C:", find_all_paths(graph, 'A', 'C'))
    print("Semua Cycle yang melewati C:", find_all_cycles(graph, 'C'))
    print("Semua Cycle yang melewati B:", find_all_cycles(graph, 'B'))
    shortest, longest = find_shortest_longest_paths(graph, 'A', 'A')
    print("Circuit terpendek dari A ke A:", shortest)
    print("Circuit terpanjang dari A ke A:", longest)
    print(f"Waktu eksekusi: {time.time() - start_time:.4f} detik")
    kembali_ke_menu()

def challenge_3():
    graph = {
        'A': ['B', 'C', 'G'], 'B': ['A', 'C', 'E'], 'C': ['A', 'B', 'D', 'F'],
        'D': ['C', 'F'], 'E': ['B', 'G', 'H'], 'F': ['C', 'D', 'I'],
        'G': ['A', 'E', 'H'], 'H': ['E', 'G', 'I', 'J'], 'I': ['F', 'H', 'J', 'K'], 'J': ['H', 'I', 'K'], 'K': ['I', 'J']
    }
    print("\n===== Challenge 3 =====")
    start_time = time.time()
    print("Semua Path dari A ke K:", find_all_paths(graph, 'A', 'K'))
    print("Semua Path dari A ke J:", find_all_paths(graph, 'A', 'J'))
    print("Semua Path dari E ke F:", find_all_paths(graph, 'E', 'F'))
    print("Semua Cycle yang melewati A:", find_all_cycles(graph, 'A'))
    print("Semua Cycle yang melewati G:", find_all_cycles(graph, 'G'))
    shortest, longest = find_shortest_longest_paths(graph, 'A', 'A')
    print("Circuit terpendek dari A ke A:", shortest)
    print("Circuit terpanjang dari A ke A:", longest)
    shortest, longest = find_shortest_longest_paths(graph, 'G', 'G')
    print("Circuit terpendek dari G ke G:", shortest)
    print("Circuit terpanjang dari G ke G:", longest)
    shortest, longest = find_shortest_longest_paths(graph, 'E', 'E')
    print("Circuit terpendek dari E ke E:", shortest)
    print("Circuit terpanjang dari E ke E:", longest)
    print(f"Waktu eksekusi: {time.time() - start_time:.4f} detik")
    kembali_ke_menu()

def kembali_ke_menu():
    kembali = input("\nMau kembali ke menu utama? (y/n): ")
    if kembali.lower() != 'y':
        print("Program selesai.")
        exit()

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for p in new_paths:
                paths.append(p)
    return paths

def find_all_cycles(graph, start, path=[], cycles=[]):
    path = path + [start]
    for node in graph[start]:
        if node == path[0] and len(path) > 2:
            cycles.append(path[:])
        elif node not in path:
            find_all_cycles(graph, node, path, cycles)
    return cycles

def find_shortest_longest_paths(graph, start, end):
    paths = find_all_paths(graph, start, end)
    if not paths:
        return None, None
    return min(paths, key=len), max(paths, key=len)

if __name__ == "__main__":
    main_menu()