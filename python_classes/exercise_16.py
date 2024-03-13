def addTuple(theTuple, lowerThan):
    addedTuple = 0
    for i in theTuple:
        if i < lowerThan:
            addedTuple += i
    print(addedTuple)

addTuple((2,3,4,5),5)
