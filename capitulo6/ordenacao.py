import random
#buble
'''
A = []
for i in range(0,10000):
    numero = random.randint(0,100)
    A.append(numero)

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
'''
#insert sort
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)
