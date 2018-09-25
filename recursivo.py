def listnum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listnum(numList[::-1])

    print(listnum([1,3,5,7,9]))