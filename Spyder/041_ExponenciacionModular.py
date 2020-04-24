def expBin(n, m):
    binary = bin(m)[2:]
    result = 1
    for d in binary:
        result *= result
        if d == '1':
            result *= n
    print (result)
expBin(2,3)
