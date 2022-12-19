for n in range(1,10):
    for m in range(1,10):
        if n >= m:
            result = n * m
            print(n, '*', m, '=', result, end="     ")
    print()