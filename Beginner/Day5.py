# Day 5
'''Ejemplo 1: Listas y Tuplas'''
# frutas = ["manzana", "pera", "uva"]
# frutas.append("mango")
# frutas.remove("pera")
# frutas_tuple = tuple(frutas)
# print(frutas_tuple)

'''Ejercicio 1'''
# numeros = [10, 20, 30, 40, 50]

# print(numeros[0])
# print(numeros[-1])
# numeros_tuple = tuple(numeros)
# print(numeros_tuple[1])

# numeros_tuple[1] = 999

'''Ejercicio 2'''
# 1. len() → longitud
# frutas = ["manzana", "uva", "mango"]
# print(len(frutas))

# 2. in → preguntar si un elemento está en la lista
# print("uva" in frutas)      # True
# print("pera" in frutas)     # False

# 3. Slicing (rebanar listas)
# [inicio:fin] → corta desde inicio hasta fin.
# [::] → puedes usar pasos.
# numeros = [10, 20, 30, 40, 50]
# print(numeros[1:4])   # [20, 30, 40]
# print(numeros[:3])    # [10, 20, 30]
# print(numeros[::2])   # [10, 30, 50]

# 4. sorted() y .sort()

# sorted() crea una nueva lista ordenada.
# .sort() modifica la lista existente.
# nums = [5, 2, 9, 1]
# print(sorted(nums))   # [1, 2, 5, 9]
# nums.sort()
# print(nums)           # [1, 2, 5, 9]

'''Ejercicio 2'''
# numeros = [8, 3, 15, 6, 1, 20]

# print(len(numeros))
# print(15 in numeros)
# print(numeros[:3])
# print(sorted(numeros))


'''Ejercicio 3'''

# valores = [100, 200, 300, 400, 500]

# print(valores[-1])
# print(valores[1:4])
# print(sorted(valores, reverse=True))


'''Ejercicio 4'''
# nombres = ["Ana", "Luis", "Pedro"]

# nombres.append("Maria")
# nombres[nombres.index("Luis")] = "Carlos"
# tuple_names = tuple(nombres)
# print(tuple_names)


'''Ejercicio 5'''
# edades = [18, 25, 30, 22, 40, 35]

# print(len(edades))
# mayores = [edad for edad in edades if edad > 25]
# print(mayores)
# print(edades.sort())


'''Ejercicio 6'''
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(nums[1::2])
# print(nums[-3:])
# tuple_nums = tuple(sorted(nums, reverse=True))
# print(tuple_nums)

'''Ejercicio 7'''

mezcla = [15, 2, 9, 8, 33, 14, 7, 20, 3]

pairs = [m for m in mezcla if m % 2 == 0]
print(pairs)
tuple_pairs = tuple(sorted(pairs))
print(tuple_pairs)

        


