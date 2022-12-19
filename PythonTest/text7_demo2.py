def delnum(n):
    print([num for num in range(1,n+1) if num % 5 < 3])
delnum(eval(input("n=")))