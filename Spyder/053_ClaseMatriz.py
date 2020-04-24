class Matriz:
    pass

    def __init__(self, f, c):
        self.__fil = f
        self.__col = c
        self.__val = []
        for i in range(f):
            fila = []
            for j in range(c):
                fila.append(0)
            self.__val.append(fila)

    def valor(self, i, j, v):
        self.__val[i][j] = v

    def dame_valor(self, i, j):
        return self.__val[i][j]

    def imprime(self):
        for i in range(self.__fil):
            fila = ""
            for j in range(self.__col):
                fila += str(self.dame_valor(i, j)) + ","
            print(fila)
        print("\n")


m = Matriz(3, 3)
m.valor(0, 1, 10)
m.valor(1, 1, 12)
m.imprime()
