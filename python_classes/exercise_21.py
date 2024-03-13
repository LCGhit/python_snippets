def wherePos(list, ele):
    positions = []
    for i in range(0, len(list)):
        if list[i] == ele:
            positions.append(i)
    print(positions)

wherePos([2,3,4,2,2],2)
