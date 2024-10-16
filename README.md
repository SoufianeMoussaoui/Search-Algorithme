# Search-Algorithme

![Search-Timeline](https://github.com/user-attachments/assets/be66175d-364b-44ee-be57-66a52df6eec5)



Searching algorithms are techniques used to locate a target element within a collection of data. 
The choice of searching algorithm depends on factors such as the size and organization of the dataset, the nature of the target element,
and the efficiency requirements of the application.
Commonly used searching algorithms include linear search, binary search, depth-first search (DFS), breadth-first search (BFS), and more. Each algorithm has its own characteristics, advantages, and limitations



# Linear Search  : 

Linear search, often known as sequential search, is the most basic search technique. 
In this type of search, you go through the entire list and try to fetch a match for a single element. 
If you find a match, then the address of the matching target element is returned. 

On the other hand, if the element is not found, then it returns a NULL value. 

Following is a step-by-step approach employed to perform Linear Search Algorithm
 
 1 Initialization : Start at the first element (index 0).

2 Comparison : Compare the current element with the target.

3 Check for Match :

     If it matches, return the index.
   
     If not, move to the next element.
   
4 Repeat : Continue until all elements are checked.

5 End of List : If the target is not found, return -1 or None


Complexity: 
𝑂
(
𝑛
)
for unsorted data.

Use Cases: Simple and unsorted data structures where simplicity is prioritized over speed.

# Binary Search

The algorithm works by repeatedly dividing the list into half portions, which can contain the item to be searched until we narrow down the possible location to just one.

## Time and Space Complexity of Binary Search Algorithm : 

| Case         | Time Complexity |
|--------------|----------------|
| Best Case    | O(1)           |
| Average Case | O(log N)       |
| Worst Case   | O(log N)       |

## Binary search vs Linear search : 

![linear-vs-binary-search](https://github.com/user-attachments/assets/78ad0758-04b3-4871-8e9b-317707aa90d8)


### Analysis:

Linear Search: The search time increases significantly as the vector size grows, which reflects its 
O(n) time complexity.

Binary Search: The search time remains almost constant or grows very slowly as the vector size increases, showing the 
O(logN) efficiency of Binary Search, which is much faster for larger datasets when compared to Linear Search.

Conclusion : the image demonstrates that Binary Search is more efficient for larger datasets compared to Linear Search, as expected due to their differing time complexities.


# Depth First Search : (DFS) 

DFS explores as deep as possible along a branch before backtracking. It uses a stack (either explicitly or through recursion) to keep track of the nodes

![image](https://github.com/user-attachments/assets/c8a8f3e6-725d-4f91-922d-dd314f8b9f7a)

We start from vertex 0, the DFS algorithm starts by putting it in the Visited list and putting all its adjacent vertices in the stack

![image](https://github.com/user-attachments/assets/7ee5b3f6-b10a-4838-9fce-c432888aea10)


Next, we visit the element at the top of stack i.e. 1 and go to its adjacent nodes. Since 0 has already been visited, we visit 2 instead.

![image](https://github.com/user-attachments/assets/45cdfac4-7bf3-43d0-bab7-f2e8582763c5)


Vertex 2 has an unvisited adjacent vertex in 4, so we add that to the top of the stack and visit it.


![image](https://github.com/user-attachments/assets/11b6b693-4ac5-49a5-bf41-42580db3d37e)

![image](https://github.com/user-attachments/assets/5c57da3e-a7d5-47a3-8d19-85b8302cc26b)

After we visit the last element 3, it doesn't have any unvisited adjacent nodes, so we have completed the Depth First Traversal of the graph.

![image](https://github.com/user-attachments/assets/b2d4c415-edf9-48fe-aae5-36a132aed192)


## DFS Pseudocode (recursive implementation)

The pseudocode for DFS is shown below. In the init() function, notice that we run the DFS function on every node. This is because the graph might have two different disconnected parts 

so to make sure that we cover every vertex, we can also run the DFS algorithm on every node.

    DFS(G, u)
      u.visited = true
      for each v ∈ G.Adj[u]
          if v.visited == false
              DFS(G,v)
     
    init() {
       For each u ∈ G
           u.visited = false
       For each u ∈ G
           DFS(G, u)
      }

## The complexity of the Depth-First Search (DFS) algorithm:

| Aspect             | Complexity            |
|--------------------|-----------------------|
| Time Complexity    | O(V + E)              |
| Space Complexity   | O(V)                  |
| Where              |                       |
| V                  | Number of vertices    |
| E                  | Number of edges       |



