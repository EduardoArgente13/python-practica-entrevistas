# Funcion que transforme un string a palabras y que regrese un diccionario con la cuenta de esas palabras

# def count_words(s):
#     if not s:
#         return None
    
#     frequency = {}
#     words = s.split()
    
#     for word in words:
#         frequency[word] = frequency.get(word, 0) + 1
        
#     return frequency

# s = "el sol brilla el cielo es azul el mar es azul"
# print(count_words(s))


#n Regresar la palabra mas frecuante de un string

# def most_frequent_word(s):
#     if not s:
#         return None
    
#     freq = {}
#     words = s.split()
    
#     for word in words:
#         freq[word] = freq.get(word, 0) + 1
    
#     most_common = ""
#     max_count = 0
    
#     for word, count in freq.items():
#         if count > max_count:
#             max_count = count
#             most_common = word
            
#     return(most_common, max_count)

# s = "el sol brilla el cielo es azul el mar es azul"
# print(most_frequent_word(s))


# Escribe una función que reciba un string s y devuelva una lista de todas las palabras que se repiten exactamente una sola vez.

# def least_frequent_words(s):
#     if not s:
#         return []
    
#     freq = {}
#     words = s.split()
    
#     for word in words:
#         freq[word] = freq.get(word, 0) + 1
    
#     res = []
    
#     for word in words:
#         if freq[word] == 1:
#             res.append(word)
    
#     return res

# s = "sol mar sol cielo luna mar tierra"
# print(least_frequent_words(s))


#Ahora con las palabras que mas se repiten

# def most_frequent_words(s):
#     if not s:
#         return []
    
#     freq = {}
#     words = s.split()
    
#     for word in words:
#         freq[word] = freq.get(word, 0) + 1
        
#     max_count = max(freq.values())
#     res = [word for word, count in freq.items() if count == max_count]
    
#     return res

# s = "sol mar sol cielo luna mar tierra"
# print(most_frequent_words(s))



# Escribe una función que reciba un string, y devuelva una lista de las palabras más frecuentes, ignorando mayúsculas y signos de puntuación.

# import re

# def most_freq_words_v2(s):
#     if not s:
#         return []
    
#     freq = {}
#     s_clean = re.sub(r'[^\w\s]', '', s.lower())
#     words = s_clean.split()
    
#     for word in words:
#         freq[word] = freq.get(word, 0) + 1
    
#     res = []
#     max_count = max(freq.values())
    
#     for word, count in freq.items():
#         if count == max_count:
#             res.append(word)
            
#     return res

# s = "El sol brilla, el mar brilla. ¡El cielo brilla también!"
# print(most_freq_words_v2(s))
    


# Haz una función que reciba un string y regrese todas las palabras más largas (limpiando signos de puntuación y normalizando mayúsculas/minúsculas).

import re

def large_words(s):
    if not s:
        return []
    
    words = re.findall(r'\b[a-záéíóúüñ]+\b', s.lower())
    
    max_len = max(len(word) for word in words)
    res = [word for word in words if len(word) == max_len]
    
    return res

s = "El avión voló sobre el océano. ¡Qué rápido!"
print(large_words(s))
    
    
    
    