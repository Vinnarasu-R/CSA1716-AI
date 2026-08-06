print("=" * 60)
print("             ARTIFICIAL INTELLIGENCE LAB")
print("         Experiment: A* Algorithm")
print("         Name   : Vinnarasu R")
print("         Reg No : 192411040")
print("=" * 60)

graph = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Node: ")
    graph[node] = {}
    e = int(input("Edges from " + node + ": "))
    for j in range(e):
        v = input("Connected node: ")
        c = int(input("Cost: "))
        graph[node][v] = c

h = {}
for i in graph:
    h[i] = int(input("Heuristic of " + i + ": "))

start = input("Start node: ")
goal = input("Goal node: ")

open_list = [start]
cost = {start: 0}
parent = {start: None}

while open_list:
    x = min(open_list, key=lambda i: cost[i] + h[i])
    open_list.remove(x)

    if x == goal:
        path = []
        while x is not None:
            path.append(x)
            x = parent[x]

        print("\nShortest Path:", path[::-1])
        print("Total Cost:", cost[goal])
        break

    for y in graph[x]:
        g = cost[x] + graph[x][y]

        if y not in cost or g < cost[y]:
            cost[y] = g
            parent[y] = x

            if y not in open_list:
                open_list.append(y)