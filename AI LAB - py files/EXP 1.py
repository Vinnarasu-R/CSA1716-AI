print("=" * 60)
print("             ARTIFICIAL INTELLIGENCE LAB")
print("         Experiment: 8 Puzzle Problem")
print("         Name   : Vinnarasu R")
print("         Reg No : 192411040")
print("=" * 60)

goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

print("Enter the initial state (9 numbers):")
state = list(map(int, input().split()))

if state == goal:
    print("\nGoal State Reached!")
    count = 0
else:
    count = 0
    for i in range(9):
        if state[i] != goal[i]:
            count += 1

print("Misplaced Tiles =", count)

print("\nInitial State:")
for i in range(0, 9, 3):
    print(state[i:i+3])

print("\nGoal State:")
for i in range(0, 9, 3):
    print(goal[i:i+3])