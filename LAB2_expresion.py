# Se acepta el valor
x=float(input("ingresa el número para evaluar la expresión\n"))
# Se desarrolla la lógica
a = x+(1/x)
b = x+(1/a)
c = x+(1/b)
y = 1/c
print("y = ",y)