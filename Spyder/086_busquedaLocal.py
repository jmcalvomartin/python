import random

def evalua(vecindad, f, valor) :
    for s in vecindad:
        temp = f(s)
        if temp < valor:
            return (s, temp)
    return None

def generaVecindad(p):
    epsilon = 0.5
    step = 0.1
    actual = p - epsilon
    vecindad = []
    while actual < p + epsilon:
        vecindad.append(actual + step)
        actual += step
    return vecindad

def busqLocal(f, iter):
    actual = random.randrange(0, 10)
    valor = f(actual)
    i = 0
    while i < iter:
        vecindad = generaVecindad(actual)
        v = evalua(vecindad, f, valor)
        if v is not None:
            actual, valor = v
        i += 1
    return actual, valor



f = lambda x: x ** 2 - 1
print(busqLocal(f, 100))
