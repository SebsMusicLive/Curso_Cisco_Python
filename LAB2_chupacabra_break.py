#Declaramos la variable y pedimos una palabra al usuario
palabra = input("Ingresa una palabra. si ingresas chupacabra dejarás el bucle:\n")

#Declaramos el while
while(palabra != ""):
    palabra = input("Ingresa una palabra. si ingresas chupacabra dejarás el bucle:\n")
    if(palabra == "chupacabra"):
        #Imprimimos el mensaje final
        print("Has dejado el bucle con éxito.")
        break
