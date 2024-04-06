# Le pedimos al usuario que ingrese c0
c0 = int(input("Ingresa un numero\n"))
# Inicializamos los pasos
steps = 0
# Declaramos mientras el número ingresado sea mayor que uno
while(c0>1):
    # Si es par dividimos en 2
    if(c0 % 2 == 0):
        c0 = c0 // 2
    else:
        # Si no es par usamos la formula c0 = (3 * c0) + 1
        c0 = (3 * c0) + 1
    # Sumamos 1 a los pasos
    steps=steps+1
    # Imprimimos c0
    print(c0)
# Imprimimos los pasos
print("Pasos =",steps)