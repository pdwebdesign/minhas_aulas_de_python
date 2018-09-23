#EXERCICIO 4 SLIDE 1
while True:
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