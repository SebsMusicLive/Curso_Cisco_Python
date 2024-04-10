my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# Recorremos la lista con un for
for i in my_list:
    if my_list[i] != my_list[i-1]:
        del(my_list[i])
    
print("La lista con elementos únicos:")
print(my_list)