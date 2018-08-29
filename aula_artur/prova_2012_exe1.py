def main():
    M = [1, 2, 3, 4, 5]
    A = f(M)
    print("A[0]:",A[0])
    print("A[1]:", A[1])
    print("A[2]:", A[2])
    print("A[3]:", A[3])
    print(A[0]/A[1], A[2]/A[3])
    print("M:",M)
def f(L):
    if len(L) == 0:
        B = [0, 0, 0, 0]
    elif L[0] % 2 > 0:
        B = g(L)
    else:
        B = [L[0]+f(L[1:])[0], 1+f(L[1:])[1], f(L[1:])[2], f(L[1:])[3]]
    return B
def g(L):
    if len(L) == 0:
        C = [0, 0, 0, 0]
    elif L[0] % 2 == 0:
        C = f(L)
    else:
        C = [g(L[1:])[0], g(L[1:])[1], L[0]+g(L[1:])[2], 1+g(L[1:])[3]]
    return C
main()