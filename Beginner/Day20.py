'''
Ejercicio: Contar vocales por inicial
Dada una lista de palabras, agrupa por inicial (minúscula) y cuenta cuántas vocales contiene cada palabra.
'''

# def count_vocals_by_initial(words):
#     if not words:
#         return {}
    
#     res = {}
#     vowels = ('a', 'e', 'i', 'o', 'u')
    
#     for word in words:
#         initial = word[0].lower()
#         count = sum(1 for c in word.lower() if c in vowels)
        
#         if initial not in res:
#             res[initial] = []
        
#         res[initial].append(word, count)
        
#     return res

# print(count_vocals_by_initial(["Ana", "Alberto", "Beatriz", "Carlos", "Carmen", "Zoe"]))


'''
📜 Enunciado:
Dada una lista de palabras, agrúpalas por la cantidad de letras que tienen.
Devuelve un diccionario donde:

La clave es un número (longitud de la palabra).

El valor es una lista de palabras con esa longitud, ordenadas alfabéticamente.
'''

# def group_by_length(words):
#     if not words:
#         return {}
    
#     res = {}
    
#     for word in words:
#         length = len(word)
#         res.setdefault(length, []).append(word)
        
#     for length in res:
#         res[length].sort()
        
#     return res

# words = ["sol", "luna", "pez", "mar", "estrella", "sol", "astro"]
# print(group_by_length(words))


'''
📜 Enunciado:
Dada una lista de palabras, encuentra cuál letra inicial (minúscula) 
es la que más palabras diferentes tiene asociadas.
''' 

# def most_common_initial(words):
#     if not words:
#         return None
    
#     res = {}
    
#     for word in words:
#         initial = word[0].lower()
        
#         res.setdefault(initial, set()).add(word)
        
#     max_initial = None
#     max_count = 0

#     for inital, word_set in res.items():
#         count = len(word_set)
        
#         if count > max_count:
#             max_initial = inital
#             max_count = count
        
        
#     return (max_initial, max_count)
        
# words = ["sol", "sombra", "luz", "luna", "lago", "libro", "fuego", "flama", "flor"]
# print(most_common_initial(words))
      

'''
Enunciado:
Dada una lista de empleados representados como tuplas (nombre, edad), agrúpalos por edad.
Para cada edad, guarda los nombres de los empleados ordenados alfabéticamente.
'''

def group_employees_by_age(data):
    if not data:
        return {}
    
    res = {}
    
    for i in data:
        age = i[1]
        name = i[0]
        res.setdefault(age, []).append(name)
        
    for age in res:
        res[age].sort()
        
    return res
    
empleados = [
    ("Ana", 30),
    ("Luis", 25),
    ("Carlos", 30),
    ("Beatriz", 25),
    ("Zoe", 40),
    ("María", 30)
]

print(group_employees_by_age(empleados))




