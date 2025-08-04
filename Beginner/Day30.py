'''
Ejercicio 1:
Tienes una lista de palabras. Queremos contar cuántas veces aparece cada palabra.
'''

# from collections import Counter

# def count_words(words):
#     if not words:
#         return {}
    
#     count = Counter(words)
    
#     return dict(count)

# words = ["manzana", "pera", "manzana", "uva", "pera", "manzana"]

# print(count_words(words))


'''
Ejercicio 2:
Tienes una lista de palabras. Queremos contar cuántas veces aparece cada letra en total (sin importar a qué palabra pertenece).
'''

# from collections import defaultdict

# def count_letters(words):
#     if not words:
#         return {}
    
#     letter_count = defaultdict(int)
    
#     for word in words:
#         for letter in word:
#             letter = letter.lower()
#             letter_count[letter] += 1
            
#     return dict(letter_count)
    
# words = ["luz", "sol", "luna"]
# print(count_letters(words))


'''
Dado un listado de palabras, queremos saber cuántas letras únicas tiene cada palabra (ignorando mayúsculas/minúsculas).
'''

# from collections import defaultdict

# def unique_letters(words):
#     if not words:
#         return {}
    
#     return {word: len(set(word.lower())) for word in words}

# words = ["sol", "luz", "luna", "sombra"]
# print(unique_letters(words))


'''
Dado un listado de palabras, crea un diccionario donde la clave sea la primera letra de cada palabra (en minúscula) y el valor sea una lista de todas las palabras que empiezan con esa letra.
'''

# from collections import defaultdict

# def group_by_first_letter(words):
#     if not words:
#         return {}
    
#     group = defaultdict(list)
    
#     for word in words:
#         initial = word[0].lower()
#         group[initial].append(word)
        
#     return group

# words = ["sol", "sombra", "luz", "luna", "mar", "montaña"]
# print(group_by_first_letter(words))


'''
Dado un listado de palabras, agrúpalas según la cantidad de letras que tienen.
'''

from collections import defaultdict

def group_by_length(words):
    if not words:
        return {}
    
    grouped = defaultdict(list)
    
    for word in words:
        length = len(word)
        grouped[length].append(word)
        
    return dict(grouped)

words = ["sol", "mar", "luz", "luna", "estrella", "sol"]
print(group_by_length(words))
    
    
            
            
    
    
    
    
    
            
            
    
    
    
