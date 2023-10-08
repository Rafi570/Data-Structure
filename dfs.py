graph={ }
flag = True
total_vertex = int(input("Enter no. of vertex: "))

for i in range(total_vertex):
    vertex = input("Enter vertex: ")
    graph[vertex] = list()
    while flag:
        child = input(f'Enter child of {vertex} (-1 for exit): ')
        if child != '-1':
            graph[vertex].append(child)
        else:
            flag = False
    flag = True

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
print("Following is the Depth-First Search")
dfs(visited, graph, '5')
