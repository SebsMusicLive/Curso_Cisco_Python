# Ingresar número de año
ano = int(input("Ingresa un número de año\n"))
# Verifica principalmente si el año pertenece al calendario Gregoriano
if(ano<1582): print("No dentro del período del calendario gregoriano")
else:
    if((ano%4)!=0): print("Año común")
    elif((ano%100)!=0): print("Año bisiesto")
    elif((ano%400)!=0): print("Año común")
    else: print("Año bisiesto")