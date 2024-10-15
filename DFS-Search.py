def dfs(graph, node, visited=None):
    # If this is the first call, initialize an empty set to keep track of visited nodes.
    if visited is None:
        visited = set()
        
    # Mark the current node as visited by adding it to the 'visited' set.
    visited.add(node)
    
    # Print the node (this is where you process the node; you can replace it with other operations).
    print(node)  # Process the node
    
    # Iterate over all the neighbors (connected nodes) of the current node.
    for neighbor in graph[node]:
        # If the neighbor has not been visited yet, call dfs recursively for that neighbor.
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


