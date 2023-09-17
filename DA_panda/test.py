from heapq import heappop as pop
from heapq import heappush as push

# Define the map
Romania_Map = {'Oradea': {'Zerind': 71, 'Sibiu': 151},
               'Zerind': {'Arad': 75, 'Oradea': 71},
               'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
               'Timisoara': {'Arad': 118, 'Lugoj': 111},
               'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
               'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
               'Drobeta': {'Mehadia': 75, 'Craiova': 120},
               'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
               'Rimnicu Vilcea': {'Craiova': 146, 'Sibiu': 80, 'Pitesti': 97},
               'Sibiu': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
               'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
               'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
               'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
               'Giurgiu': {'Bucharest': 90},
               'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
               'Neamt': {'Iasi': 87},
               'Iasi': {'Neamt': 87, 'Vaslui': 92},
               'Vaslui': {'Iasi': 92, 'Urziceni': 142},
               'Hirsova': {'Urziceni': 98, 'Eforie': 86},
               'Eforie': {'Hirsova': 86}
               }

# Define the node class
class Node:
    def __init__(self, name, parent=None, path_cost=0):
        self.name = name
        self.parent = parent
        self.path_cost = path_cost

# Define the heuristic values for each city to Bucharest
heuristic_values = {
    'Oradea': 380, 'Zerind': 374, 'Arad': 366, 'Timisoara': 329,
    'Lugoj': 244, 'Mehadia': 241, 'Drobeta': 242, 'Craiova': 160,
    'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Fagaras': 176, 'Pitesti': 100,
    'Bucharest': 0, 'Giurgiu': 77, 'Urziceni': 80, 'Neamt': 234,
    'Iasi': 226, 'Vaslui': 199, 'Hirsova': 151, 'Eforie': 161
}

# Define the Best-First Search function
def best_first_search(start_city, goal_city, heuristic_values):
    open_list = [(heuristic_values[start_city], start_city)]
    closed_list = set()

    while open_list:
        open_list.sort(reverse=True)  # Sort by heuristic value in descending order
        _, current_city = open_list.pop()

        if current_city == goal_city:
            # Reconstruct the path
            path = [current_city]
            while current_city != start_city:
                current_city = parent_map[current_city]
                path.append(current_city)
            path.reverse()
            return path

        closed_list.add(current_city)

        for neighbor, cost in Romania_Map[current_city].items():
            if neighbor not in closed_list and neighbor not in parent_map:
                parent_map[neighbor] = current_city
                open_list.append((heuristic_values[neighbor], neighbor))

    return None

# Example usage
start_city = 'Drobeta'
goal_city = 'Bucharest'
parent_map = {}  # Store parent cities to reconstruct the path

path = best_first_search(start_city, goal_city, heuristic_values)

if path:
    total_cost = sum(Romania_Map[path[i]][path[i + 1]] for i in range(len(path) - 1))
    print(path, total_cost)
else:
    print("Path not found")
