print("=" * 60)
print("             ARTIFICIAL INTELLIGENCE LAB")
print("         Experiment: Water Jug Problem")
print("         Name   : Vinnarasu R")
print("         Reg No : 192411040")
print("=" * 60)

j1 = int(input("Enter capacity of Jug 1: "))
j2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

a = 0
b = 0

print("\nSteps:")

while b != target:
    if a == 0:
        a = j1
    elif b == j2:
        b = 0
    else:
        t = min(a, j2 - b)
        a -= t
        b += t

    print("Jug1 =", a, "Jug2 =", b)

print("\nTarget Reached!")
