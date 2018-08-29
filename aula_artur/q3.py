def maxfreq(nome):
    a = open(nome,"r")
    f = []

    for l in a:
        l = a.readline()
        for p in l:
            if len(p) >= 3:
                if p in f:
                    f[p] +=1
                else:
                    f.append(p)

    print(f)
    m = None
    for p in f:
        m = p
    m = 0

def main ():
    arq = "texto.txt"
    maxfreq(arq)
    print("palavra:", "freq. rel.:")

main()