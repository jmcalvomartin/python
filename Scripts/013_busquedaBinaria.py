def busquedaBinRec (elementos, inicio, fin, x):
    if inicio is fin:
        return elementos [inicio] is x
    centro = ((fin - inicio) // 2) + inicio

    if x < elementos [centro]:
        return busquedaBinRec (elementos, inicio, centro, x)
    elif x > elementos [centro]:
        return busquedaBinRec (elementos, centro + 1, fin, x)
    return True

def busquedaBin (elementos, x):
    if elementos is None or len(elementos) is 0:
        return False
    return busquedaBinRec (elementos, 0, len (elementos) - 1, x)

print(busquedaBin([1, 2, 3, 5], 1))
print(busquedaBin([1, 2, 3, 5], 7))
