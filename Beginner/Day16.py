'''
Dadas dos listas de palabras, devuelve una nueva lista con las palabras que:

Aparecen en ambas listas

Sin duplicados

En el orden en que aparecen en la primera lista
'''

# def ordered_interseccion(list1, list2):
#     if not list1 and not list2:
#         return []
    
#     res = []
#     list2_set = set(list2)
#     already_added = set()
    
#     for word in list1:
#         if word in list2_set and word not in already_added:
#             res.append(word)
#             already_added.add(word)
            
#     return res

# print(ordered_interseccion(["a", "b", "c", "d", "a"], ["c", "a", "e", "b"]))

          
'''
Dadas dos listas de palabras, devuelve una nueva lista con las palabras que:

Aparecen una sola vez en la primera lista

Aparecen una sola vez en la segunda lista

Están presentes en ambas listas

Mantén el orden de aparición según la primera lista
'''

# def ordered_unique_intereccions(list1, list2):
#     if not list1 or not list2:
#         return []
    
#     res = []
#     list2_set = set(list2)
#     already_added = set()
    
#     for word in list1:
#         if word in list2_set and word not in already_added:
#             res.append(word)
#             already_added.add(word)
            
#     return res

# list1 = ["gato", "perro", "gato", "pato", "pez"]
# list2 = ["pez", "pato", "pez", "gato"]

# print(ordered_unique_intereccions(list1, list2))


'''
Enunciado:
Dada una lista de palabras, devuelve un diccionario donde:

Las claves sean las longitudes de las palabras

Los valores sean listas de palabras con esa longitud

Las palabras deben aparecer en el orden original
'''

# def grouped_by_lenght(words):
#     if not words:
#         return {}
    
#     result = {}
    
#     for word in words:
#         result.setdefault(len(word), []).append(word)
        
#     return result
    
# words = ["sol", "luna", "pez", "mar", "estrella"]
# print(grouped_by_lenght(words))



'''
Enunciado:
Dada una lista de palabras, devuelve un diccionario donde:

La clave es la letra inicial de cada palabra

El valor es el número de veces que aparecen palabras con esa letra"
'''

# def count_by_initial(words):
#     if not words:
#         return {}
    
#     res = {}
    
#     for word in words:
#         initial = word[0]
#         res[initial] = res.get(initial, 0) + 1
        
#     return res
    

# print(count_by_initial(["sol", "silla", "luna", "lago", "serpiente", "mar"]))


'''
Enunciado:
Dada una lista de palabras, devuelve un diccionario donde:

Cada clave es la letra inicial de una palabra

Cada valor es una lista con todas las palabras que comienzan con esa letra

El orden dentro de cada lista debe respetar el orden original
'''

# def group_by_initial(words):
#     if not words:
#         return {}
    
#     res = {}
    
#     for word in words:
#         initial = word[0]
#         res.setdefault(initial, []).append(word)
        
#     return res

# entrada = ["sol", "silla", "luna", "lago", "serpiente", "mar"]
# print(group_by_initial(entrada))


'''
Enunciado:
Dada una lista de palabras, devuelve un diccionario donde:

Cada clave es una letra inicial

Cada valor es otro diccionario que contiene:

"palabras": la lista de palabras que empiezan con esa letra

"conteo": el número de veces que aparece esa inicial
'''

# def group_and_count_initials(words):
#     if not words:
#         return {}
    
#     res = {}
    
#     for word in words:
#         initial = word[0]
        
#         if initial not in res:
#             res[initial] = {"words" : [], "count" : 0}
            
#         res[initial]["words"].append(word)
#         res[initial]["count"] += 1
        
        
#     return res

# entrada = ["sol", "silla", "serpiente", "luna", "lago", "mar"]
# print(group_and_count_initials(entrada))

    
 


