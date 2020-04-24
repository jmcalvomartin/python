for i in map((lambda x: x * 2), [1, 2, 3]):
    print(i)


for i in map((lambda x, y: x * y), [1, 2, 3], [4, 5, 6]):
    print(i)


for i in filter((lambda x: x > 0), range(-5, 5)):
    print(i)
