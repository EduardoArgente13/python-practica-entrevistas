'''
Dado un arreglo de enteros nums, devuelve True si existen dos valores dentro de una ventana de longitud k que difieran como mucho en t unidades (no necesariamente iguales).

🔍 En resumen:
Queremos saber si existe:

abs(i - j) <= k

abs(nums[i] - nums[j]) <= t
'''
# from sortedcontainers import SortedList

# def contains_nearby_almost_duplicates(nums, k, t):
#     if t < 0 or k <= 0:
#         return False

#     window = SortedList()
    
#     for i, num in enumerate(nums):
#         pos = window.bisect_left(num - t)
        
#         if pos < len(window) and abs(window[pos] - num) <= t:
#             return True
        
#         window.add(num)
        
#         if len(window) > k:
#             window.remove(nums[i - k])
#     return False
    

'''
Dado un arreglo (lista) de palabras, devuelve una nueva lista que contenga solo las palabras únicas, en el orden en que aparecieron por primera vez.
'''

# def ordered_words(words):
#     if not words:
#         return []
    
#     uniques = []
#     seen = set()
    
#     for word in words:
#         if word not in seen:
#             uniques.append(word)
#             seen.add(word)
        
#     return uniques

# print(ordered_words(["perro", "gato", "perro", "pez", "loro", "gato"]))



'''
Dada una lista de palabras, crea una nueva lista que contenga solo las palabras que aparecieron más de una vez, 
sin repetirlas y en el orden en que ocurrieron por segunda vez.
'''

# def repeated_words(words):
#     if not words:
#         return []
    
#     repeated = []
#     seen = {}
    
#     for word in words:
#         seen[word] = seen.get(word, 0) + 1
#         if seen[word] == 2:
#             repeated.append(word)
            
#     return repeated
            
# entrada = ["sol", "luna", "sol", "estrella", "luna", "sol"]
# print(repeated_words(entrada))  # ['sol', 'luna']


