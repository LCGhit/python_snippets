def replaceMe(lst, old, new):
    for i in lst:
        if i == old:
            i = new
    print(lst)
replaceMe([1,2,3,2,4,],2,'a')
