#EXERCICIO 2 SLIDE 2

A = [-1,5,10,-3,8,15,4,-10,9,0]

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