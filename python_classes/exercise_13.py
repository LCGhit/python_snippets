newNum = input("write a number\n")
def soma_digitos_pares(someNum):
    evenNum = 0
    for i in someNum:
        if int(i)%2 == 0:
            evenNum += int(i)
        else:
            continue
    print(evenNum)
soma_digitos_pares(newNum)
