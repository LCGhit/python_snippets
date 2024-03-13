def greatestDic(dic):
    greatestValue = 0
    for value in dic.values():
        if int(value) > int(greatestValue):
            greatestValue = value
    print(greatestValue)

newDic = {"111":10, "122":14, "133":16, "144":10}
greatestDic(newDic)
