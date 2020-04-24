def amenaza(tablero, f, c):
    # Inicio Diagonales
    if f >= c:
        f0 = f - c
        c0 = 0
    else:
        f0 = 0
        c0 = c - f
    if c <= len(tablero)-1-f:
        f1 = 0
        c1 = f + c
    else:
        f1 = f - (len(tablero))
        c1 = len(tablero)-1 - c

    for i in range(len(tablero)):
        # Chequeo Columna
        if i is not f and tablero[i][c]:
            return True
        # Chequeo Fila
        if i is not c and tablero[f][i]:
            return True
        # Chequeo Diagonal 1
        if i is not c and valida(f0, c0, len(tablero)) \
        and tablero[f0][c0]:
            return True
        # Chequeo Diagonal 2
        if i is not c and valida(f1, c1, len(tablero))\
        and tablero[f1][c1]:
            return True
        f0 += 1
        c0 += 1
        f1 -= 1
        c1 -= 1
    return False


def valida(f, c, n):
    return f >= 0 and c>=0 and f < n and c < n


def reinas(tablero, n):
    if n is 0:
        return True
    dim = len(tablero)
    col = dim - n
    for f in range(dim):
        if not amenaza(tablero, f, col):
            tablero[f][col] = True
            if reinas(tablero, n - 1):
                return True
            tablero[f][col] = False
    return False


tablero = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
	  ]
if reinas(tablero, 4):
    print (tablero)


