# Title:
# Implement depth first search algorithm and Breadth First Search algorithm, Use an undirected
# graph and develop a recursive algorithm for searching all the vertices of a graph or tree data
# structure.


# 1].BFS

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = []
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
    visited.append(node)
    queue.append(node)
    while queue:    
        m = queue.pop(0)     
        print (m, end = " ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    # function calling

Output:

comp@comp-HP-EliteDesk-800-G1-SFF:~$ python3 bfs.py
Following is the Breadth-First Search
5 3 7 2 4 8

# 2].DFS

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
visited = []
def dfs(visited, graph, node):  #function for dfs
    if node not in visited:
        print (node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
print("Following is the Depth-First Search")
dfs(visited, graph, '5')

# Output:

# comp@comp-HP-EliteDesk-800-G1-SFF:~$ python3 dfs.py
# Following is the Depth-First Search
# 5
# 3
# 2
# 4
# 8
# 7
