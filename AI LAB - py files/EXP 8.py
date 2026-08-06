print("=" * 60)
print("      ARTIFICIAL INTELLIGENCE LAB PROGRAM")
print("      Name   : Vinnarasu R")
print("      Reg No : 192411040")
print("=" * 60)

visited = []
queue = []

graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    vertex = input("Enter vertex: ")
    neighbors = input("Enter adjacent vertices (space separated): ").split()
    graph[vertex] = neighbors

def bfs(start):
    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

start = input("\nEnter starting vertex: ")

print("\nBFS Traversal:")
bfs(start)