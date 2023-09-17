import random

Romania_Map = {'Oradea':[('Zerind',71),('Sibiu',151)],
               'Zerind':[('Arad',75),('Oradea',71)],
               'Arad':[('Zerind',75),('Sibiu',140),('Timisoara',118)],
               'Timisoara':[('Arad',118),('Lugoj',111)],
               'Lugoj':[('Timisoara',111),('Mehadia',75)],
               'Mehadia':[('Lugoj',70),('Drobeta',75)],
               'Drobeta':[('Mehadia',75),('Craiova',120)],
               'Craiova':[('Drobeta',120),('Rimnicu Vilcea',146),('Pitesti',138)],
               'Rimnicu Vilcea':[('Craiova',146),('Sibiu',80),('Pitesti',97)],
               'Sibiu':[('Oradea',151),('Arad',140),('Fagaras',99),('Rimnicu Vilcea',80)],
               'Fagaras':[('Sibiu',99),('Bucharest',211)],
               'Pitesti':[('Rimnicu Vilcea',97),('Craiova',138),('Bucharest',101)],
               'Bucharest':[('Fagaras',211),('Pitesti',101),('Giurgiu',90),('Urziceni',85)],
               'Giurgiu':[('Bucharest',90)],
               'Urziceni':[('Bucharest',85),('Vaslui',142),('Hirsova',98)],
               'Neamt':[('Iasi',87)],
               'Iasi':[('Neamt',87),('Vaslui',92)],
               'Vaslui':[('Iasi',92),('Urziceni',142)],
               'Hirsova':[('Urziceni',98),('Eforie',86)],
               'Eforie':[('Hirsova',86)]           
              }

class PathFindingAgent(object):
    def __init__(self, Map):
        self.map = Map
        self.route = []
        self.total_cost = 0
        self.visited_cities = set()

    def solve(self, start, end, budget=999999):
        self.route.append(start)
        self.current_city = start
        tries = 0
        
        while tries < 10:  # Limit the number of tries to prevent infinite loops
            if self.current_city == end:
                return self.route, self.total_cost

            # Make a list of next cities (neighbors) that haven't been visited
            unvisited_cities = [
                (city, cost) for city, cost in self.map[self.current_city]
                if city not in self.visited_cities
            ]

            if not unvisited_cities:
                # No unvisited neighbors, backtrack
                if len(self.route) < 2:
                    # No more backtracking possible, stop
                    return self.route, self.total_cost
                else:
                    # Backtrack to the previous city and mark the current city as visited
                    self.visited_cities.add(self.current_city)
                    self.route.pop()
                    self.current_city = self.route[-1]
            else:
                # Choose a random unvisited neighbor
                next_city, cost = random.choice(unvisited_cities)
                self.visited_cities.add(self.current_city)
                self.route.append(next_city)
                self.total_cost += cost
                self.current_city = next_city

                # Check if the budget constraint is met
                if self.total_cost > budget:
                    return self.route, self.total_cost

            tries += 1

        # If the search is not successful within the given tries, suggest increasing the budget
        return [], self.total_cost, "Increase the budget for a better result"

if __name__ == '__main__':
    agent = PathFindingAgent(Romania_Map)
    route, total_cost, message = agent.solve('Bucharest', 'Arad', budget=500)
    
    if route:
        print("Route:", route)
        print("Total Cost:", total_cost)
    else:
        print("No path found or budget too low:", message)
