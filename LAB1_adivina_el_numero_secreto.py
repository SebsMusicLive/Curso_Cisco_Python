print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

# Le pedimos al usuario un número
numero_usuario = int(input("Ingresa un número: \n"))

# Declaramos secret_number
secret_number = 777

while(numero_usuario != secret_number): numero_usuario = int(input("¡Ja, ja! ¡Estás atrapado en mi bucle! Vuelve a intentarlo\n"))

print(secret_number,"¡Bien hecho, muggle! Eres libre ahora.")