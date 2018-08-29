def div(a,b):
    try:
        return a/b
    except Exception as e:
        print(e)

print(div(4,0))