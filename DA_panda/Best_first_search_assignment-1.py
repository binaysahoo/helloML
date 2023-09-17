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


from heapq import heappop as pop
from heapq import heappush as push


#Todos:
#1. Define the two functions from the pseudo code
#2. Provide, at least, 5 test cases


#=================================================================================
# Define the Best-First Search function


def expand(problem, node):
    # Get the current state from the node
    s = node.state
    
    # Initialize a list to store the child nodes
    child_nodes = []

    # Iterate over available actions in the problem's action space for the current state
    for action in problem.ACTIONS(s):
        # Apply the action to obtain the new state s'
        s_prime = problem.RESULT(s, action)
        
        # Calculate the cost of the action
        action_cost = problem.ACTION_COST(s, action, s_prime)
        total_cost = node.path_cost + action_cost
        
        # Create a new child node
        child_node = Node(state=s_prime, parent=node, action=action, path_cost=total_cost)
        
        # Add the child node to the list
        child_nodes.append(child_node)

    # Yield the generated child nodes
    for child in child_nodes:
        yield child

# Example usage:
# Define your problem-specific ACTIONS, RESULT, and ACTION-COST functions as needed.
# Then, you can use the `expand` function to generate child nodes from a parent node.

def best_first_search(problem, f):
    # Create the initial node with the problem's initial state
    initial_node = Node(state=problem.INITIAL)
    
    # Create the frontier as a priority queue ordered by f with the initial node
    frontier = [(f(initial_node), initial_node)]
    
    # Create a lookup table 'reached' with the initial state mapped to the initial node
    reached = {problem.INITIAL: initial_node}
    
    while frontier:
        # Pop the node with the highest priority from the frontier
        _, current_node = pop(frontier)
        
        # If the current node's state is a goal state, return it as a solution
        if problem.IS_GOAL(current_node.state):
            return current_node
        
        # Expand the current node to generate child nodes
        for child_node in expand(problem, current_node):
            s = child_node.state
            if s not in reached or child_node.path_cost < reached[s].path_cost:
                # Update 'reached' and add the child node to the frontier
                reached[s] = child_node
                push(frontier, (f(child_node), child_node))
    
    # If no solution is found, return None to indicate failure
    return None

# Example usage:
# Define your problem-specific INITIAL, IS_GOAL, ACTIONS, RESULT, and ACTION-COST functions as needed.
# Define an evaluation function 'f' for prioritizing nodes based on your problem's requirements.
# Then, use the 'best_first_search' function to find a solution node.
def INITIAL():
    return 'Arad'

def IS_GOAL(state):
    return state == 'Bucharest'

def ACTIONS(state):
    # Return a list of valid actions for the given state (e.g., neighboring cities)
    return list(Romania_Map[state].keys())

def RESULT(state, action):
    # Return the resulting state after taking the given action
    return action

def ACTION_COST(state, action, next_state):
    # Return the cost of taking the given action from the current state to the next state
    return Romania_Map[state][next_state]

# Define the evaluation function 'f' based on the path cost to prioritize nodes
def f(node):
    return node.path_cost

# Your Romania_Map and other relevant data structures should be defined.

# Perform the Best-First Search
start_city = INITIAL()
goal_city = 'Bucharest'

# Initialize the frontier with the initial node
initial_node = Node(state=start_city)
frontier = [(f(initial_node), initial_node)]

# Initialize a lookup table 'reached' with the initial state mapped to the initial node
reached = {start_city: initial_node}

while frontier:
    _, current_node = pop(frontier)
    if IS_GOAL(current_node.state):
        # Reconstruct the path from the goal node to the start node
        path = []
        while current_node:
            path.append(current_node.state)
            current_node = current_node.parent
        path.reverse()
        total_cost = sum(
            ACTION_COST(path[i], path[i + 1], path[i + 2]) for i in range(len(path) - 2)
        )
        print(path, total_cost)
        break

    for child_node in expand(current_node, ACTIONS, RESULT, ACTION_COST):
        s = child_node.state
        if s not in reached or child_node.path_cost < reached[s].path_cost:
            reached[s] = child_node
            push(frontier, (f(child_node), child_node))