from collections import deque
# The deque from the collections module is used to implement a queue (FIFO) for BFS, 
# allowing efficient appending and popping from both ends.

def bfs(graph, start):
    # Initialize a set to keep track of visited nodes.
    visited = set()
    
    # Create a queue (FIFO) and add the starting node to it.
    queue = deque([start])
    
    # Continue the loop as long as there are nodes in the queue.
    while queue:
        # Remove the node from the front of the queue (dequeue).
        node = queue.popleft()
        
        # If the node hasn't been visited, process it.
        if node not in visited:
            print(node)  # Process the node (you can replace this with any other operation).
            
            # Mark the node as visited by adding it to the 'visited' set.
            visited.add(node)
            
            # Add all unvisited neighbors of the current node to the queue.
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)



