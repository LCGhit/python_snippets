def double(tup):
    newList = []
    for i in tup:
        newList.insert(len(newList), i)
        newList.insert(len(newList), i)
    print(tuple(newList))

double("123")
