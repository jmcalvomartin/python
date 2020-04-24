def maxPalindromo(s):
    # Crea matriz de nxn con 1s en la diagonal
    m = [[(1 if j == i else 0) for i in range(len(s))]
           for j in range(len(s))]

    for i in range(1, len(s)):
        # Completar diagonal desde max(0,k)
        j = i
        for k in range(len(s)-i):
            if s[k] is s[j]:
                if i is 1:
                    m[k][j] = 2
                else:
                    m[k][j] = 2 + m[k+1][j-1]
            else:
                m[k][j] = max(m[k][j-1], m[k+1][j])
            j += 1
    return m[0][len(s)-1]

print('LSLP', maxPalindromo('locolocoyloquito'))
