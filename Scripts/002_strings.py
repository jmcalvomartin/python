print("Cadena Vacia", str())
print("Repr en Cadena", str(["A", "h"]))
print("Copia de Cadena", str("MJ"))


# introducimos funciones para aplicar slicing a una cadena
def practica(stringTest):
    str = stringTest[0:3]
    print(str)

def practica2(stringTest):
    str = stringTest[1:4]
    print(str)


practica("Me gusta escribir python")

practica2("Aprendo python")
