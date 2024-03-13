def keyFinder(dic, val):
    keysArray = []
    for key in dic.keys():
        if dic[key] == val:
            keysArray.append(key)
    print(keysArray)

newDict = {"keyOne": "value1", "keyTwo": "value2", "keyThree": "value3", "keyFour": "value1"}
keyFinder(newDict, "value1")
