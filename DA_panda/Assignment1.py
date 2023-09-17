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
    def __init__(self, name, parent=None, path_cost=0, map=Romania_Map):
        self.name = name
        self.parent = parent
        self.map = map
        self.path_cost = path_cost

# Function to retrieve the from heapq import heappop as pop
from heapq import heappop as pop
from heapq import heappush as push

# Define the BEST-FIRST-SEARCH function
def BEST_FIRST_SEARCH(problem, f):
    # Initialize the start node
    node = Node(problem.INITIAL)
    frontier = [(f(node), node)]  # Priority queue ordered by f(node)
    reached = {node.name: node}  # Each value is a tuple (parent, action)

    while frontier:
        _, node = pop(frontier)  # Use the heuristic value for prioritization
        if problem.IS_GOAL(node.name):
            return node

        for child in EXPAND(problem, node):
            s = child.name
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                push(frontier, (f(child), child))  # Use the heuristic value for prioritization
    return 'failure'

# Define the EXPAND function
def EXPAND(problem, node):
    s = node.name
    for action in problem.ACTIONS(s):
        s1 = action
        cost = node.path_cost + problem.ACTION_COST(s, action, s1)
        yield Node(name=s1, parent=node, path_cost=cost)

# Example usage:
class Problem():
    def __init__(self, source, destination) -> None:
        self.INITIAL=source
        self.GOAL=destination
    
    def IS_GOAL(self, city):
        if city==self.GOAL: return True
        return False
    
    def ACTIONS(self, state):
        return list(Romania_Map[state].keys())
    
    def ACTION_COST(self,parent, action, child):
        if Romania_Map[parent]:
            return Romania_Map[parent][action]
        return False
    


testcases=[
    ('Arad', 'Bucharest'),
    ('Drobeta', 'Pitesti'),
    ('Sibiu', 'Neamt'),
    ('Neamt', 'Craiova'),
    ('Vaslui', 'Eforie'),
]

for source, destination in testcases:
    problem=Problem(source, destination)

    result = BEST_FIRST_SEARCH(problem, f=lambda node: node.path_cost)  
    if result == 'failure':
        print('No path found.')
    else:
        path = []
        cost = 0
        while result.parent:
            path.insert(0, result.name)
            cost += problem.ACTION_COST(result.parent.name, result.name, result.name)
            result = result.parent
        path.insert(0, problem.INITIAL)
        print('Shortest path:', path, cost)
        