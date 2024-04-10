my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

#Si quieres empezar desde el dato de índice 0 se puede hacer de esta manera
new_list_1 = my_list[:3]
print(new_list_1)

#Si quieres terminar con el dato de len(my_list)
new_list_2 = my_list[3:]
print(new_list_2)

#Al omitir el start y el end se crea una copia de toda la lista
new_list_3 = my_list[:]
print(new_list_3)

#La función del puede usar rebanadas para poder eliminar varios elementos de la lista
del my_list[1:3]
print(my_list)

#También puedes eliminar todos a la vez
del my_list[:]
print(my_list)

#OJO CON ESTO
my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list)
 