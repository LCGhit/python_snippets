def checkShot(dic, tup):
    xCoord = ord((tup[0]).lower())-96
    yCoord = int(tup[1])
    for key, value in dic.items():
        dicXcoord = ord(value[0].lower())-96
        dicXcoordRange = 0
        dicYcoord = int(value[1])
        dicYcoordRange = 0
        if key == "aircraftCarrier":
            dicXcoordRange = dicXcoord+5
            dicYcoordRange = dicYcoord+1
        if (xCoord >= dicXcoord and xCoord < dicXcoordRange) and (yCoord >= dicYcoord and yCoord < dicYcoordRange):
            print("hit " + value)
            return
        else:
            continue
    print("water")
board = {"aircraftCarrier": "B3", "Cruiser": "F2", "Destroyer": "B5", "Tugboat": "I7"}

checkShot(board, ("F", 3))
