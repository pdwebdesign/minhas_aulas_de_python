'''while True:
    a = int(input("digite numero 1"))
    b = int(input("digite numero 2"))
    c = int(input("digite numero 3"))

    if a > b:
        if b > c:
            print(a,b,c)
        elif a > c:
            print(a,c,b)
        else:
            print(c,a,b)
    elif a > c:
        print(b,a,c)
    elif b > c:
        print(b,c,a)
    else:
        print(c,b,a)
'''

A = [1970,2020,1960,2010,2012,2017]
def ordenar(A):
    if len(A) <= 1:
        print(A)
    else:
        for j in range(0,len(A)):
            for i in range(0,len(A)-1):
                if A[i]>A[i+1]:
                    Aux = A[i+1]
                    A[i+1] = A[i]
                    A[i] = Aux
        print(A)

ordenar(A)


