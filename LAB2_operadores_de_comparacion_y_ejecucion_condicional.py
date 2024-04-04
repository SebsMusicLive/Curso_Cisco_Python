# Recibimos la palabra 
planta = input("Ingresa el nombre de una planta \n")
# Comprobamos si la planta es "Espatifilo"

if(planta == "ESPATIFILO" or planta == "Espatifilo"):
    print("Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!")
elif(planta == "espatifilo"):
    print("No, ¡quiero un gran Espatifilo!")
else:
    print("¡Espatifilo!, ¡No",planta,"!")