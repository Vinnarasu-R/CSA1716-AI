print("=" * 60)
print("             ARTIFICIAL INTELLIGENCE LAB")
print("         Experiment: Travelling Salesman Problem")
print("         Name   : Vinnarasu R")
print("         Reg No : 192411040")
print("=" * 60)

from itertools import permutations

d = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cost = 999
path = ()

for p in permutations([1, 2, 3]):
    c = d[0][p[0]] + d[p[0]][p[1]] + d[p[1]][p[2]] + d[p[2]][0]

    if c < cost:
        cost = c
        path = (0,) + p + (0,)

print("\nShortest Path:", path)
print("Minimum Cost:", cost)