def isPrime(number):
    for i in range(2, int(number)):
        if(float(number)%i!=0 and i!=number):
            continue
        elif(float(number)%i==0 and int(i)==int(number)):
            print("is prime number")
            break
        else:
            print("not a prime number")


isPrime(input("what number would you like to check\n"))
