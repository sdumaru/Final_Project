""" Graph data structure to store flights """

class Graph:
    """ Graph or Map between flights. """
    def __init__(self):
        # Initialize an empty adjacency list
        self.adjacency_list = {}

    def add_node(self, node):
        """ Add a node (cities) to the graph """
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2):
        """ Add Bi-directional flight route between 2 nodes or cities """
        if node1 in self.adjacency_list and node2 in self.adjacency_list:
            self.adjacency_list[node1].append(node2)
            self.adjacency_list[node2].append(node1)

    def remove_edge(self, node1, node2):
        """ Remove Bi-directional flight route between 2 nodes or cities """
        if node1 in self.adjacency_list and node2 in self.adjacency_list:
            if node2 in self.adjacency_list[node1]:
                self.adjacency_list[node1].remove(node2)
            if node1 in self.adjacency_list[node2]:
                self.adjacency_list[node2].remove(node1)

    def display(self):
        """ Display the graph as an adjacency list """
        for origin, destination in self.adjacency_list.items():
            print(f"{origin} -> {destination}")

    def shortest_path(self, start_node, end_node):
        """ BFS implementation to find the shortest path between two nodes (cities) """
        if start_node not in self.adjacency_list or end_node not in self.adjacency_list:
            return None                         # Return None if either node is not in the graph

        queue = [(start_node, [start_node])]    # Queue stores (current node, path to current node)
        visited = set()

        while queue:
            current_node, path = queue.pop(0)

            if current_node == end_node:
                return path                     # Return the path if we reach the destination node

            if current_node not in visited:
                visited.add(current_node)

                # Add neighbors to the queue with updated paths
                for neighbor in self.adjacency_list[current_node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

        # Return None if no path exists between start_node and end_node
        return None

# Example Usage
graph = Graph()

# Add cities to the graph
graph.add_node('Austin')
graph.add_node('Boston')
graph.add_node('Chicago')
graph.add_node('Dallas')
graph.add_node('Peoria')

# Add edges to the graph
graph.add_edge('Austin', 'Boston')
graph.add_edge('Austin', 'Chicago')
graph.add_edge('Boston', 'Dallas')
graph.add_edge('Chicago', 'Peoria')
graph.add_edge('Dallas', 'Peoria')

# Display the adjacency list of the graph
print("Graph Representation (Adjacency List):")
graph.display()

path1 = graph.shortest_path("Austin", "Peoria")
if path1:
    print(f"Shortest path between Flight Austin and Flight Boston: {' -> '.join(path1)}")
else:
    print("No path found between Flight Austin and Flight Boston")
