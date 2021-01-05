x = [i for i in range(5)]
print(x)


x = [1, 2, 3, 4, 5]
y = [str(i) for i in x]
print(y) # Convertimos integer en string 

x = ['1', '2', '3', '4', '5']
y = [int(i) for i in x]
print(y) # Convertimos string en integer 


vec = [[1,2,3], [4,5,6], [7,8,9]]
flatVec = [num for elem in vec for num in elem]
print(flatVec) # Unimos listas 

# Cambiamos clave por valor en un diccionario
my_dict = {1:"dog", 2:"cat", 3:"hamster"}
print(my_dict)
print( {value:key for key, value in my_dict.items()} )
