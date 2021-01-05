import itertools

for i in itertools.filterfalse(lambda x: x<=2, [11,2.3,-11]):
    print (i)