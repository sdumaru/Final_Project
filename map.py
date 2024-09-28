""" Graph data structure to store flights """

import heapq
import time
import random

class Graph:
    """ Graph or Map between flights. """
    def __init__(self):
        self.adjacency_list = {}            # Adjacency list to store nodes and their connections
        self.weights = {}                   # Dictionary to store weights of edges
        self.shortest_path_cache = {}       # Cache to store results of shortest path calculations

    def add_node(self, node):
        """ Add a node (city) to the graph. """
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2, weight=1):
        """ Add a bi-directional flight route between 2 nodes (cities) with a weight. """
        if node1 in self.adjacency_list and node2 in self.adjacency_list:
            self.adjacency_list[node1].append(node2)
            self.adjacency_list[node2].append(node1)

            # Add weights for both directions
            self.weights[(node1, node2)] = weight
            self.weights[(node2, node1)] = weight

    def remove_edge(self, node1, node2):
        """ Remove Bi-directional flight route between 2 nodes or cities """
        if node1 in self.adjacency_list and node2 in self.adjacency_list:
            if node2 in self.adjacency_list[node1]:
                self.adjacency_list[node1].remove(node2)
            if node1 in self.adjacency_list[node2]:
                self.adjacency_list[node2].remove(node1)

        # Remove the weights associated with the edge
        if (node1, node2) in self.weights:
            del self.weights[(node1, node2)]
        if (node2, node1) in self.weights:
            del self.weights[(node2, node1)]

        # Clear cache as the structure has changed
        self.shortest_path_cache.clear()

    def display(self):
        """ Display the graph's adjacency list and weights. """
        print("Adjacency List:")
        for origin, destinations in self.adjacency_list.items():
            print(f"{origin} -> {destinations}")
        print("\nWeights:")
        for (node1, node2), weight in self.weights.items():
            print(f"{node1} <-> {node2} : {weight}")

    def dijkstra(self, start_node, end_node):
        """ Dijkstra's algorithm to find the shortest path between two nodes based on edge weights. """
        # Priority queue to hold nodes to be explored
        pq = []
        # Start with the source node with a distance of 0
        heapq.heappush(pq, (0, start_node))

        # Distances dictionary to hold shortest path estimates
        distances = {node: float('inf') for node in self.adjacency_list}
        distances[start_node] = 0

        # Previous node dictionary to reconstruct the path
        previous_nodes = {node: None for node in self.adjacency_list}

        while len(pq) != 0:
            current_distance, current_node = heapq.heappop(pq)

            # If we reach the destination node, reconstruct and return the path
            if current_node == end_node:
                path = []
                while previous_nodes[current_node] is not None:
                    path.insert(0, current_node)
                    current_node = previous_nodes[current_node]
                path.insert(0, start_node)
                return path, current_distance

            # Explore neighbors of the current node
            for neighbor in self.adjacency_list[current_node]:
                edge_weight = self.weights[(current_node, neighbor)]
                distance = current_distance + edge_weight

                # Only consider this path if it's better than any known path so far
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        # If no path is found, return None
        return None, float('inf')

    def shortest_path(self, start_node, end_node):
        """ Wrapper function to find and cache the shortest path using Dijkstra's algorithm. """
        # Check if the path is already cached
        if (start_node, end_node) in self.shortest_path_cache:
            print(f"Using cached result for shortest path between {start_node} and {end_node}")
            print(f"Shortest path between {start_node} and {end_node}: "
                  f"{' -> '.join(self.shortest_path_cache[(start_node, end_node)][0])} "
                  f"with total distance {self.shortest_path_cache[(start_node, end_node)][1]}")
            return self.shortest_path_cache[(start_node, end_node)]

        # Validate nodes
        if start_node not in self.adjacency_list or end_node not in self.adjacency_list:
            print(f"One of the nodes {start_node} or {end_node} does not exist in the graph.")
            return None

        # Calculate the shortest path using Dijkstra's algorithm
        path, distance = self.dijkstra(start_node, end_node)

        # Cache the result
        if path:
            self.shortest_path_cache[(start_node, end_node)] = (path, distance)
            print(f"Cached the result for shortest path between {start_node} and {end_node}")

        # Display and return the result
        if path:
            print(f"Shortest path between {start_node} and {end_node}: {' -> '.join(path)} with total distance {distance}")
            return path
        else:
            print(f"No path found between {start_node} and {end_node}.")
            return None

def generate_cities(no_cities):
    """ Generate random city names """
    return [f"City_{i}" for i in range(no_cities)]

# Create the graph
graph = Graph()

# Add 500 cities (nodes)
num_cities = 500
cities = generate_cities(num_cities)

for city in cities:
    graph.add_node(city)

# Add random edges with weights (distances)
num_edges = random.randint(num_cities, num_cities * 2)

for _ in range(num_edges):
    city1, city2 = random.sample(cities, 2)  # Ensure we have two different cities
    weight = random.randint(100, 3000)  # Random distance between 100 and 3000 miles
    graph.add_edge(city1, city2, weight)

# Display the graph
# graph.display()

# Measure execution time for finding the shortest path
start_time = time.perf_counter_ns()
shortest_path = graph.shortest_path('City_0', 'City_400')
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print(f"Execution time first time: {execution_time} nano seconds")

# Find and display the shortest path again to demonstrate caching
start_time = time.perf_counter_ns()
shortest_path = graph.shortest_path('City_0', 'City_400')  # This should use the cached result
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print(f"Execution time after getting from cache: {execution_time} nano seconds")
