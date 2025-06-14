# Shortest Path Algorithm (Dijkstra's Algorithm)

This Python script implements **Dijkstra's algorithm** to compute the shortest path from a starting node to all other nodes in a weighted graph.

## How It Works

- Uses a dictionary-based adjacency list to represent the graph.
- Calculates the shortest distances from the starting node to all others.
- Tracks the actual paths taken.
- Can display all shortest paths or just a specific target.

## Example Graph

```python
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

Usage

shortest_path(my_graph, 'A')       # Show all shortest paths from 'A'
shortest_path(my_graph, 'A', 'F')  # Show shortest path from 'A' to 'F'

File Structure
markdown
Copy code
Python_learning/
└── shortest_path_algorithm/
    ├── shortest_path.py
    └── README.md

Concepts Covered
Graph traversal

Greedy algorithm

Path reconstruction

Dijkstra's shortest path algorithm

Author
Abhishek Anand