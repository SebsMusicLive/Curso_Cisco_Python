#El + en cadenas se usa para concatenar, es decir String + String
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")

#El * se usa para replicar el número de veces que señales para replicar, así:
""" String * Number
ó   Number * String"""

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
