def biss(year):
    if((year%4==0 and year%100!=0) or (year%100!=0 and year%400==0)):
        print(str(year)+" is bissexto")
    else:
        print(str(year)+" is not bissexto")
biss(int(input("input year: \n")))
