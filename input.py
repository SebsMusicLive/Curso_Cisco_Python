# Función input sin argumento
print('Dime lo que sea...')
anything = input()
print('mmm... ', anything, '...¿En serio?')

# Función input con argumento
print('Con argumentos\n')
any = input('Dime lo que sea...')
print('mmm...', any, "...¿En serio?")

# La función input no sirve para aceptar números, sólo cadenas
# Probando un mensaje de error TypeError.

anything = input("Ingresa un número: ")
something = anything ** 2.0
print(anything, "al cuadrado es", something)
