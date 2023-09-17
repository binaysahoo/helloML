# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09 13:23:41 2017

@author: xfang13

The Romania problem
"""
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
    def solve(self, start, end):
        flag = True
        self.route.append(start)
        self.current_city = start
        while flag:
            if self.current_city == end:
                flag = False
            else:
                #Make a list of next cities: Observing
                cities = [city for city, cost in self.map[self.current_city]]
                #Make a list of next costs: Observing
                costs = [cost for city, cost in self.map[self.current_city]]
                #See if the destination is in the next cities' list
                try:
                    i = cities.index(end)
                    self.current_city = end
                    self.route.append(self.current_city)
                    self.total_cost += costs[i]
                #if not then random walk    
                except ValueError:
                    next_city, cost = random.sample(self.map[self.current_city],1)[0]
                    #Add the current cost to the total
                    self.total_cost += cost
                    #Set next city to the current city
                    self.current_city = next_city
                    #Add the current city to the route
                    self.route.append(self.current_city)
                
                
if __name__ == '__main__':
    agent = PathFindingAgent(Romania_Map)
    agent.solve('Bucharest', 'Arad')
    print (agent.route, agent.total_cost)                