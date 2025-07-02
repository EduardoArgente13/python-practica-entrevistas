'''
Enunciado:
Dada una lista de palabras, agrúpalas en un diccionario donde:

La clave principal es la vocal inicial de cada palabra (a, e, i, o, u)

El valor es una lista de palabras que comienzan con esa vocal

Ignora palabras que no comiencen con vocal.
'''

# def group_by_vocals(words):
#     if not words:
#         return {}
    
#     vocals = {'a', 'e', 'i', 'o', 'u'}
#     res = {v:[] for v in vocals}
    
#     for word in words:
#         initial = word[0].lower()
#         if initial in vocals:
#             res[initial].append(word)
    
#     res = {k: v for k, v in res.items() if v}
    
#     return res 

# entrada = ["árbol", "oso", "sol", "elefante", "uva", "casa", "iguana", "estrella"]
# print(group_by_vocals(entrada))


'''
📜 Enunciado:
Dada una lista de palabras, crea un diccionario donde:

La clave es la letra inicial de la palabra

El valor es una lista de palabras únicas que comienzan con esa letra

Pero solo incluye palabras que aparezcan exactamente una vez en la lista original.
'''

# from collections import Counter

# def group_by_initial(words):
#     if not words:
#         return {}
    
#     res = {}
#     count = Counter(words)
    
#     for word in words:
#         if count[word] == 1:
#             initial = word[0]
            
#             if initial not in res:
#                 res[initial] = []
            
#             res[initial].append(word)
            
#     return res
            

'''
Dada una lista de tuplas, retorna las tuplas que aparecen más de una vez.
'''

# from collections import Counter

# def return_repeating_tuples(tuples):
#     if not tuples:
#         return []
    
#     count = Counter(tuples)
#     res = []
    
#     for tup in count:
#         if count[tup] > 1:
#             res.append(tup)
            
#     return res
        
# def return_repeating_tuples(tuples):
#     count = Counter(tuples)
#     return [tup for tup, freq in count.items() if freq > 1]
    
    
# entrada = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (7, 8)]
# print(return_repeating_tuples(entrada))


'''
📜 Enunciado:
Dada una lista de coordenadas representadas como tuplas (x, y), devuelve un diccionario donde:

Cada clave sea la tupla (x, y)

Cada valor sea el número de veces que esa coordenada aparece
'''

# def count_coordinates(coordenates):
#     if not coordenates:
#         return {}
    
#     res = {}
    
#     for coor in coordenates:
#         res[coor] = res.get(coor, 0) + 1
            
#     return res

# ####

# from collections import Counter

# def count_coordinates(coordinates):
#     return Counter(coordinates)


# entrada = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
# print(count_coordinates(entrada))
   
'''
Dada una lista de tuplas (nombre, categoría), agrupa todos los nombres por categoría.
'''

# def group_by_category(data):
#     if not data:
#         return {}
    
#     res = {}
    
#     for i in data:
#         category = i[1]
        
#         if category not in res:
#             res[category] = []
            
#         res[category].append(i[0])
        
#     return res

# entrada = [
#     ("Ana", "admin"),
#     ("Luis", "editor"),
#     ("María", "admin"),
#     ("Carlos", "lector"),
#     ("Lucía", "editor"),
# ]

# print(group_by_category(entrada))


'''
📜 Enunciado:
Dada una lista de pares de usuarios representados como tuplas (a, b), encuentra todos los pares que son relaciones simétricas.

Es decir, si está el par (a, b), y también (b, a)... entonces es una relación simétrica.
'''

# def find_symmetric_pairs(pairs):
#     if not pairs:
#         return []
    
#     res = []
#     pairs_set = set(pairs)
    
#     for a, b in pairs:
#         if (b, a) in pairs_set and a < b:
#             res.append((a, b))

#     return res

# relaciones = [
#     ("Ana", "Luis"),
#     ("Luis", "Ana"),
#     ("Carlos", "Lucía"),
#     ("Lucía", "Carlos"),
#     ("María", "José"),
#     ("Pedro", "Juan")
# ]

# print(find_symmetric_pairs(relaciones))


'''
📜 Enunciado:
Dada una lista de pares (a, b), encuentra aquellos que no tienen su versión invertida (b, a) en la lista.

Por ejemplo, si está ("Ana", "Luis") pero no ("Luis", "Ana"), entonces debe aparecer en la salida.
'''

# def find_unique_elements(pairs):
#     if not pairs:
#         return []
    
#     res = []
#     set_pairs = set(pairs)
    
#     for a, b in pairs:
#         if (b, a) not in set_pairs:
#             res.append((a, b))
            
#     return res
            
# pairs = [
#     ("Ana", "Luis"),
#     ("Carlos", "Lucía"),
#     ("Lucía", "Carlos"),
#     ("Pedro", "Juan"),
#     ("Juan", "Pedro"),
#     ("Diego", "Mario")
# ]

# print(find_unique_elements(pairs))


'''
Ejercicio 2: Relación de amistad mutua y no mutua
Dada una lista de pares (a, b), identifica:

Las relaciones mutuas: donde existen ambos (a, b) y (b, a)

Las no mutuas: donde solo uno de los dos está
'''

# def mutual_non_mutual_friendship(pairs):
#     if not pairs:
#         return []
    
#     mutual = []
#     non_mutual = []
#     set_pairs = set(pairs)
    
#     for a, b in pairs:
#         if (b, a) not in set_pairs:
#             non_mutual.append((a, b))
#         elif (b, a) in set_pairs and a < b:
#             mutual.append((a, b))
        
#     return {"mutual" : mutual, "non mutual" : non_mutual}

# relaciones = [
#     ("Ana", "Luis"),
#     ("Luis", "Ana"),
#     ("Carlos", "Lucía"),
#     ("María", "José"),
#     ("Pedro", "Juan")
# ]

# print(mutual_non_mutual_friendship(relaciones))

