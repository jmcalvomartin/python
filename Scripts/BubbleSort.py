#Creamos una funcion llamada BubbleSort y le pasamos como parametro una lista
def bubblesort(lista):
    #En el loop for recorremos la lista de izquierda a derecha
    for i in range (len(lista)):
        #usamos "len(l)" para saber la longitud de nuestra lista
        longitud = len(lista) - 1
        #En el While realiza el recorrido de derecha a izquierda, llegando hasta el indice actual del primer ciclo que lo contiene.
        while longitud >= i:
            #La sentencia if simplemente compara elementos adyacentes y los entercambia en caso de que se cumpla la condicion.
            if lista[longitud] < lista[longitud -1]:
                #usamos una variable "temp" para realizar el intercambio de posicion.
                temp = lista[longitud]
                lista[longitud] = lista[longitud-1]
                lista[longitud-1] = temp
            longitud-=1
    #devolvemos el valor de la lista ya ordenado.
    return lista

print ("Introduce una secuencia de numeros desordenada y separada por comas:")
valores=input(); #Introducimos los valores por teclado
list = valores.split(",") #Separamos los valores por la coma para introducirlos como una lista
print(bubblesort(list)) #Imprimimos la lista ordenada
