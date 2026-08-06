print("=" * 60)
print("      ARTIFICIAL INTELLIGENCE LAB PROGRAM")
print("      Name   : Vinnarasu R")
print("      Reg No : 192411040")
print("=" * 60)

visited = []
graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    vertex = input("Enter vertex: ")
    neighbors = input("Enter adjacent vertices (space separated): ").split()
    graph[vertex] = neighbors

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for i in graph[node]:
            dfs(i)

start = input("\nEnter starting vertex: ")

print("\nDFS Traversal:")
dfs(start)