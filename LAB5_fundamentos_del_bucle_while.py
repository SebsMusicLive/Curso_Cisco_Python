# El usuario ingresa la cantidad de bloques
blocks = int(input("Ingresa el número de bloques: "))

# Declaramos e inicializamos las variables
height=0
utilizados = 0
por_fila = 1

# Declaramos el while
while True:
    # Sumamos de a uno a los bloques utilizados
    utilizados += por_fila
    # Comparamos si los utilizados son mayores que los bloques disponibles
    if utilizados > blocks:
        # Si es así, rompemos el ciclo
        break
    # Sumamos uno a la altura y a los bloques por fila
    height += 1
    por_fila += 1

# Imprimimos la altura
print("La altura de la pirámide:", height)