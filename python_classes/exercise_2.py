operation = input("1. F to C\n2. C to F\n")
while(operation != "-1"):
    if operation == "1":
        fahr = input("How many degrees to convert to Celsius?")
        print((int(fahr)-32)*(5/9))
    elif operation == "2":
        cels = input("How many degrees to convert to Fahrenheit?")
        print(int(cels)*(9/5)+32)
    elif operation == "-1":
        print("Goodbye")
    else:
        print("invalid input")
        operation = input("1. F to C\n2. C to F\n")
        continue
