# paso 1
beatles = []
print("Paso 1:", beatles)

# paso 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# paso 3
for i in range(2):
    new_member=input('Ingresa un nuevo miembro en la banda')
    beatles.append(new_member)
print("Paso 3:", beatles)

# paso 4
del(beatles[4])
del(beatles[3])
print("Paso 4:", beatles)

# paso 5
beatles.insert("Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))

