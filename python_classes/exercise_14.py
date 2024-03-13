def insert_dig(inNum, outNum):
    if inNum == "":
        print(outNum)
        return outNum
    else:
        outNum += inNum[len(inNum)-1]
        insert_dig(inNum.replace(inNum[len(inNum)-1], ""), outNum)

insert_dig(input("Number to invert\n"), "")
