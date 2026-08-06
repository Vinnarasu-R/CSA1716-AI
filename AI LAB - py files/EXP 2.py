print("=" * 60)
print("             ARTIFICIAL INTELLIGENCE LAB")
print("         Experiment: 8 Queen Problem")
print("         Name   : Vinnarasu R")
print("         Reg No : 192411040")
print("=" * 60)

N = int(input("Enter the number of queens: "))

x = [-1] * N

def safe(r, c):
    for i in range(c):
        if x[i] == r or abs(x[i] - r) == abs(i - c):
            return False
    return True

def queen(c):
    if c == N:
        print("\nSolution:")
        for i in range(N):
            print(x[i], end=" ")
        print("\n")

        print("Chessboard:")
        for i in range(N):
            for j in range(N):
                if x[j] == i:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
        return True

    for r in range(N):
        if safe(r, c):
            x[c] = r
            if queen(c + 1):
                return True

    return False

if not queen(0):
    print("No Solution")
