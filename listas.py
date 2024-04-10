numbers = [10, 5, 7, 2, 1] #Creamos la lista con los respectivos números
print("Contenido de la lista:", numbers)  # Imprimiendo contenido de la lista original.
 
numbers[0] = 111 #Llamamos la posición del primer número y asignamos el nuevo valor
print("Nuevo contenido de la lista: ", numbers)  # Contenido actual de la lista.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

del numbers[1]  # Eliminando el segundo elemento de la lista.
print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

###

#Aunque parezca extraño los indices negativos funcionan

"""El -1 es el último elemento de la lista,
el -2 es el penúltimo elemento de la lista"""

# Se imprime el último elemento de la lista
print("Último elemento de la lista:", numbers[-1])

# Se imprime el penúltimo elemento de la lista
print("Penúltimo elemento de la lista:", numbers[-2])