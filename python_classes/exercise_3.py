box = 0
dig = int(input("input a number (-1 to exit):\n"))
while dig != -1:
    box = box*10+dig
    dig = int(input("input a number (-1 to exit):\n"))
print("The number is: ", box)
