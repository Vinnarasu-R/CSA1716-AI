print("=" * 60)
print("             ARTIFICIAL INTELLIGENCE LAB")
print("         Experiment: Missionaries and Cannibals")
print("         Name   : Vinnarasu R")
print("         Reg No : 192411040")
print("=" * 60)

from collections import deque

q = deque([((3, 3, 0), [])])
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
seen = set()

while q:
    (m, c, b), path = q.popleft()

    if (m, c, b) in seen:
        continue

    seen.add((m, c, b))

    if (m, c, b) == (0, 0, 1):
        print("\nSolution Path:")
        for state in path + [(m, c, b)]:
            print(state)
        break

    for x, y in moves:
        nm = m - x if b == 0 else m + x
        nc = c - y if b == 0 else c + y

        if 0 <= nm <= 3 and 0 <= nc <= 3:
            if (nm == 0 or nm >= nc) and (3 - nm == 0 or 3 - nm >= 3 - nc):
                q.append(((nm, nc, 1 - b), path + [(m, c, b)]))
