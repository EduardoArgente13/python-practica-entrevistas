'''
📜 Enunciado:
Dada una lista de palabras, agrúpalas solo si inician con vocal (a, e, i, o, u).
Para cada vocal, genera un diccionario con:

"words": lista de palabras que empiezan con esa vocal

"count": cuántas palabras hay

"avg_length": longitud promedio de esas palabras
'''

# def analyze_vocal_words(words):
#     if not words:
#         return {}

#     res = {}
#     vowels = ('a', 'e', 'i', 'o', 'u')

#     for word in words:
#         initial = word[0].lower()
        
#         if initial in vowels:
#             if initial not in res:
#                 res[initial] = {'words' : [], 'count' : 0, 'avg_length' : 0.0}
#             res[initial]['words'].append(word)
#             res[initial]['count'] += 1
    
#     max_avg = 0
#     best_vowel = None
    
#     for initial in res:
#         word_list = res[initial]['words']
#         total_len = sum(len(w) for w in word_list)
#         count = res[initial]['count']
#         res[initial]['avg_length'] = round(total_len/count, 2)
        
       
#         if res[initial]['avg_length'] > max_avg:
#             max_avg = res[initial]['avg_length']
#             best_vowel = initial
    
#     return {best_vowel: res[best_vowel]} if best_vowel else {}

# words = ["agua", "sol", "aire", "uva", "universo", "eco", "idea", "luz"]
# print(analyze_vocal_words(words))


'''
Ejercicio: Clasificación por longitud y conteo de iniciales
📜 Enunciado:
Dada una lista de palabras, agrúpalas por longitud.
Para cada longitud, crea un diccionario donde las claves sean las letras iniciales y los valores indiquen cuántas palabras empiezan con esa letra.
'''

# def count_initials_by_length(words):
#     if not words:
#         return {}

#     res = {}

#     for word in words:
#         length = len(word)
#         initial = word[0].lower()
        
#         if length not in res:
#             res[length] = {}
#         res[length][initial] = res[length].get(initial, 0) + 1

#     return res

# words = ["sol", "sombra", "sal", "luz", "luna", "lago", "libro", "flama", "eco", "estrella"]
# print(count_initials_by_length(words))


'''
Ejercicio: Palabras clasificadas por paridad de longitud
📜 Enunciado:
Dada una lista de palabras, clasifícalas según si su longitud es par o impar.
Devuelve un diccionario con dos claves: "even" y "odd", cada una conteniendo:

una lista con las palabras de esa categoría

la cantidad total de letras que suman

el promedio de longitud de las palabras en esa categoría
'''

def classify_by_parity(words):
    if not words:
        return {}

    res = {
        'even': {'words': [], 'total_length': 0, 'avg_length': 0.0},
        'odd': {'words': [], 'total_length': 0, 'avg_length': 0.0}
    }

    for word in words:
        length = len(word)
        group = 'even' if length % 2 == 0 else 'odd'
        res[group]['words'].append(word)
        res[group]['total_length'] += length

    for group in res:
        words_list = res[group]['words']
        if words_list:
            res[group]['avg_length'] = round(res[group]['total_length'] / len(words_list), 2)

    return res

words = ["sol", "luna", "cielo", "nube", "azul", "río"]
print(classify_by_parity(words))






