'''
Ejercicio 1: Ordenar empleados por edad
📜 Enunciado:
Dada una lista de tuplas (nombre, edad), devuelve la lista ordenada de menor a mayor edad.
'''

# def order_by_age(data):
#     if not data:
#         return []
    
#     return sorted(data, key=lambda x: x[1])

# empleados = [
#     ("Ana", 34),
#     ("Luis", 29),
#     ("María", 40),
#     ("Carlos", 25)
# ]

# print(order_by_age(empleados))


'''
📜 Enunciado:
Dada una lista de empleados como tuplas (nombre, edad), ordénalos:

Primero por edad (de menor a mayor)

Si tienen la misma edad, ordena por nombre (alfabéticamente)
'''

# def sort_by_age_and_name(data):
#     if not data:
#         return []
    
#     return sorted(data, key=lambda x: (x[1], x[0]))

# empleados = [
#     ("Ana", 34),
#     ("Luis", 29),
#     ("María", 34),
#     ("Carlos", 29),
#     ("Zoe", 40),
#     ("Beatriz", 34)
# ]

# print(sort_by_age_and_name(empleados))


'''
📜 Enunciado:
Dada una lista de tuplas (nombre, edad), agrupa los empleados por edad.
Devuelve un diccionario donde la clave sea la edad, y el valor sea una lista con los nombres de los empleados de esa edad.
'''

# def group_by_age(data):
#     if not data:
#         return {}
    
#     res = {}
    
#     for name, age in data:
#         if age not in res:
#             res[age] = []
#         res[age].append(name)
        
#     ordered_res = dict(sorted(res.items()))
        
#     return ordered_res

# empleados = [
#     ("Ana", 34),
#     ("Luis", 29),
#     ("María", 34),
#     ("Carlos", 29),
#     ("Zoe", 40),
#     ("Beatriz", 34)
# ]

# print(group_by_age(empleados))


'''
 Enunciado:
Dada una lista de tuplas (nombre, edad), 
devuelve una lista con los nombres de los 
empleados que tengan al menos cierta edad mínima, 
ordenados alfabéticamente.
'''

# def older_users(data, minimum_age):
#     if not data:
#         return []
    
#     res = []
    
#     for name, age in data:
#         if age >= minimum_age:
#             res.append(name)
    
#     return sorted(res)

# empleados = [
#     ("Ana", 34),
#     ("Luis", 29),
#     ("María", 40),
#     ("Carlos", 25),
#     ("Zoe", 41),
#     ("Beatriz", 34)
# ]

# print(older_users(empleados, 34))


'''
📜 Enunciado:
📜 Enunciado:
Dada una lista de nombres (solo strings), 
agrúpalos por su letra inicial.
Devuelve un diccionario donde:

La clave es la letra inicial (minúscula).
El valor es una lista de nombres ordenados alfabéticamente.
'''

def group_and_sort_by_initial(names):
    if not names:
        return {}
    
    res = {}
    
    for name in names:
        initial = name[0].lower()
        res.setdefault(initial, []).append(name)
        
    for initial in res:
        res[initial].sort()
        
    return res
    
nombres = [
    "Ana", "Alberto", "Beatriz", "Bruno", 
    "Carlos", "Carmen", "Zoe", "Zaira", "Zara"
]

print(group_and_sort_by_initial(nombres))




