print("=" * 60)
print("             ARTIFICIAL INTELLIGENCE LAB")
print("         Experiment: Cryptarithmetic Problem")
print("         Name   : Vinnarasu R")
print("         Reg No : 192411040")
print("=" * 60)

from itertools import permutations

for p in permutations(range(10), 8):
    S, E, N, D, M, O, R, Y = p

    if S != 0 and M != 0:
        send = 1000 * S + 100 * E + 10 * N + D
        more = 1000 * M + 100 * O + 10 * R + E
        money = 10000 * M + 1000 * O + 100 * N + 10 * E + Y

        if send + more == money:
            print("\nSolution Found:")
            print("SEND  =", send)
            print("MORE  =", more)
            print("MONEY =", money)
            break
