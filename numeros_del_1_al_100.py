# Con while
# Declaramos la variable que nos va a servir de contador
i = 0
# Definimos el while
while i <= 100:
    # Imprimimos los números
    print(i)
    # Aumentamos de uno en uno
    i += 1

#Con for
num = 1
for i in range(100):
    print(num)
    num+=1

# Range() puede tener dos argumentos range(valor inicial, valor final)
for i in range(2, 8):
    print("El valor de i es", i)

# Range() puede tener tres argumentos range(valor inicial, valor final, incremento)
for i in range(2, 8, 3):
    print("El valor de i es", i)

