'''
Enunciado:
Dada una lista de palabras, agrupa por inicial (minúscula) y devuelve la palabra más larga de cada grupo.
'''

# def longest_word_by_initial(words):
#     if not words:
#         return {}
    
#     res = {}
#     longest = ""
    
#     for word in words:
#         initial = word[0].lower()
        
#         if initial not in res or len(word) > len(res[initial]):
#             res[initial] = word
            
#     return res
        
# print(longest_word_by_initial(["sol", "sombra", "luz", "luna", "lago", "libro", "flor", "fuego"]))


'''
📜 Enunciado:
Dada una lista de palabras, agrúpalas por letra inicial (minúscula).
Para cada inicial, cuenta cuántas palabras hay de cada longitud.
'''

# def group_and_count_by_initial_and_length(words):
#     if not words:
#         return {}
    
#     res = {}
    
#     for word in words:
#         initial = word[0].lower()
#         length = len(word)
        
#         if initial not in res:
#             res[initial] = {}
        
#         res[initial][length] = res[initial].get(length, 0) + 1
        
#     return res

# words = ["sol", "sol", "sombra", "sal", "luz", "luna", "libro", "lago", "fuego", "flor", "flama"]
# print(group_and_count_by_initial_and_length(words))


'''
Enunciado:
Dada una lista de palabras, agrúpalas por letra inicial (minúscula).
Para cada grupo, calcula el promedio de longitud de las palabras que empiezan con esa letra.
'''

# def average_length_by_initial(words):
#     if not words:
#         return {}

#     res = {}

#     for word in words:
#         initial = word[0].lower()
        
#         res.setdefault(initial, []).append(word)
        
#     for initial in res:
#         palabras = res[initial]
#         promedio = sum(len(p) for p in palabras) / len(palabras)
#         res[initial] = round(promedio, 2)

#     return res

# words = ["sol", "sombra", "sal", "luz", "luna", "lago", "libro", "flama"]
# print(average_length_by_initial(words))


'''
📜 Enunciado:
Dada una lista de palabras, construye un diccionario donde la clave sea la letra inicial (minúscula) y el valor sea otro diccionario con esta estructura:

"count": cuántas palabras comienzan con esa letra

"avg_length": longitud promedio de esas palabras

"longest": la palabra más larga que comienza con esa letra

"shortest": la palabra más corta que comienza con esa letra
'''

# def analysis_by_initial(words):
#     if not words:
#         return {}

#     res = {}

#     # Agrupar palabras por letra inicial
#     for word in words:
#         initial = word[0].lower()
#         res.setdefault(initial, []).append(word)

#     # Reemplazar la lista por el análisis
#     for initial in res:
#         wrds = res[initial]
#         count = len(wrds)
#         avg = round(sum(len(w) for w in wrds) / count, 2)
#         longest = max(wrds, key=len)
#         shortest = min(wrds, key=len)

#         res[initial] = {
#             "count": count,
#             "avg_length": avg,
#             "longest": longest,
#             "shortest": shortest
#         }

#     return res


# words = ["sol", "sombra", "sal", "luz", "luna", "lago", "libro", "flama"]
# print(analysis_by_initial(words))



