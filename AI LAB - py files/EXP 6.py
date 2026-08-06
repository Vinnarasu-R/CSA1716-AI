print("=" * 60)
print("             ARTIFICIAL INTELLIGENCE LAB")
print("         Experiment: Vacuum Cleaner Problem")
print("         Name   : Vinnarasu R")
print("         Reg No : 192411040")
print("=" * 60)

A = input("Enter Room A status (Dirty/Clean): ")
B = input("Enter Room B status (Dirty/Clean): ")

print("\nInitial State")
print("Room A =", A)
print("Room B =", B)

print("\nVacuum starts at Room A")

if A.lower() == "dirty":
    print("Room A is Dirty")
    print("Cleaning Room A...")
    A = "Clean"
else:
    print("Room A is already Clean")

print("\nMove to Room B")

if B.lower() == "dirty":
    print("Room B is Dirty")
    print("Cleaning Room B...")
    B = "Clean"
else:
    print("Room B is already Clean")

print("\nFinal State")
print("Room A =", A)
print("Room B =", B)

print("\nAll rooms are clean.")
