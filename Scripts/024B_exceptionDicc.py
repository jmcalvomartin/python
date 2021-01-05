my_dict = {"a": 1, "b": 2, "c": 3}
my_list = []

for key, value in my_dict.items():
    my_list = [key, value]

    print (my_dict)

    print(my_list)

try:
    value = my_list[1]
    value = my_dict["a"]

except IndexError:
    print("Este índice no existe!")
except KeyError:
    print("Esta llave no está en el diccionario!")
except:
    print("Ha pasado alguna otra cosa!")
else:
    print("No hay error!")

finally:
    print("Este código se ejecuta independientemente de que haya una excepción")



