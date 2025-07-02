'''
Dada una lista de palabras, devuelve un diccionario donde:

Cada clave es una longitud de palabra

El valor es cuántas veces aparece una palabra con esa longitud
'''

# def count_length(words):
#     if not words:
#         return {}
    
#     seen = {}
    
#     for word in words:
#         length = len(word)
        
#         seen[length] = seen.get(length, 0) + 1
        
#     return seen
            
# entrada = ["sol", "luna", "mar", "estrella", "pez", "lago"]
# print(count_length(entrada))
    

'''
Dada una lista de palabras, devuelve un diccionario como este:

{
  "s": {"cortas": 1, "largas": 2},
  "l": {"cortas": 2, "largas": 0},
  "m": {"cortas": 1, "largas": 0}
}
'''

# def clasify_by_length_size(words):
#     if not words:
#         return {}
    
#     res = {}
    
#     for word in words:
#         initial = word[0]
        
#         if initial not in res:
#             res[initial] = {"initial" : initial, "words" : {"short" : 0, "long" : 0}}
            
#         if len(word) <= 4:
#             res[initial]["words"]["short"] += 1
#         else:
#             res[initial]["words"]["long"] += 1
            
#     return res


'''
Enunciado:
Dada una lista de palabras, crea un diccionario donde:

Cada clave principal es la letra inicial

Cada valor es otro diccionario

Ese segundo diccionario tiene como claves las longitudes exactas de las palabras que empiezan con esa inicial

Cada valor es una lista de palabras con esa longitud e inicial
'''

# def group_by_length_initial(words):
#     if not words:
#         return {}
    
#     res = {}
    
#     for word in words:
#         initial = word[0]
#         length = len(word)
        
#         if initial not in res:
#             res[initial] = {}
            
#         if length not in res[initial]:
#             res[initial][length] = []
            
#         res[initial][length].append(word)
        
#     return res

# entrada = ["sol", "ser", "silla", "sal", "luna", "lago", "luz", "serpiente"]
# print(group_by_length_initial(entrada))
           

'''
Enunciado:
Dada una lista de palabras, construye un diccionario con esta forma:

Clave principal: letra inicial

Clave secundaria: longitud de la palabra

Valor: cuántas palabras tienen esa inicial y longitud
'''        

# def count_by_initial_and_length(words):
#     if not words:
#         return {}
    
#     res = {}
    
#     for word in words:
#         initial = word[0]
#         length = len(word)
        
#         if initial not in res:
#             res[initial] = {}
            
#         res[initial][length] = res[initial].get(length, 0) + 1
            
#     return res

# entrada = ["sol", "ser", "sal", "silla", "serpiente", "luna", "luz", "lago"]
# print(count_by_initial_and_length(entrada))
         
        
'''
 Enunciado:
Dada una lista de palabras, devuelve un diccionario donde:

La clave principal es la letra inicial

La clave secundaria es la longitud de la palabra

El valor es otro diccionario con:

"palabras" → lista de palabras que coinciden

"conteo" → cuántas hay
'''

# def group_and_count_words(words):
#     if not words:
#         return {}
    
#     res = {}
    
#     for word in words:
#         initial = word[0]
#         lenght = len(word)
        
#         if initial not in res:
#             res[initial] = {}
        
#         if lenght not in res[initial]:
#             res[initial][lenght] = {"words" : [], "count" : 0}
            
#         res[initial][lenght]["words"].append(word)
#         res[initial][lenght]["count"] += 1
        
#     return res

# entrada = ["sol", "ser", "sal", "silla", "serpiente", "luna", "luz", "lago"]
# print(group_and_count_words(entrada))


'''
Dada una lista de palabras, construye un diccionario donde:

La clave principal es la inicial de la palabra

La clave secundaria es la longitud

El valor es una lista de palabras que coinciden con esa inicial y esa longitud

PERO: solo incluye iniciales que aparecen más de una vez en la lista.
'''

# from collections import Counter

# def group_if_initial_repeated(words):
#     if not words:
#         return {}
    
#     res = {}
#     initials = Counter()
    
#     for word in words:
#         initials[word[0]] += 1
    
#     for word in words:
#         initial = word[0]
#         length = len(word)
        
#         if initials[initial] < 2:
#             continue
        
#         if initial not in res:
#             res[initial] = {}
        
#         if length not in res[initial]:
#             res[initial][length] = []
        
#         res[initial][length].append(word)
            
#     return res

# entrada = ["sol", "ser", "luz", "luna", "mar", "sal", "lago", "mesa", "pez"]
# print(group_if_initial_repeated(entrada))
  
        
    
        
        
        
        


   
