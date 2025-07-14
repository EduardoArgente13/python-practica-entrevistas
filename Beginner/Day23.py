
# Separar una frase por palabras
# frase = "gato perro ave gato rana perro gato"
# palabras = frase.split()
# # print(palabras)


# Encontrar los indices de na palabra repetida
# for i in range(len(palabras)):
#     if palabras[i] == 'perro':
#         # print(i)
#         pass
        

# indexes = [0, 3, 6]

# for i in range(len(indexes) - 1):
#     distance = indexes[i + 1] - indexes[i] - 1
#     # print(distance)  
#     pass  


# distances = [2, 2]
# min_distance = 3
# approved = all(d >= min_distance for d in distances)
# print(approved)




'''
Dado una frase (una cadena de texto), el objetivo es encontrar la palabra más larga que se repita en la frase, con la condición de que entre una ocurrencia de esa palabra y la siguiente (o anterior) haya al menos una cierta cantidad de "espacios" o "palabras" de separación.
'''

# def findMaxGapRepeatedWord(phrase, min_dist):
#     if not phrase:
#         return False
    
#     words = phrase.split()
#     res = {}
    
#     for i in range(len(words)):
#         word = words[i].lower()
#         if word not in res:
#             res[word] = [i]
#         else:
#             res[word].append(i)
            
#     options = []
    
#     for word, pos in res.items():
#         if len(pos) < 2:
#             continue
        
#         distances = [pos[i+1] - pos[i] - 1 for i in range(len(pos)- 1)]
        
#         if all(d >= min_dist for d in distances):
#             options.append(word)
            
#     if not options:
#         return None
    
#     answer = max(options, key=len)
        
#     return answer

# print(findMaxGapRepeatedWord("gato perro ave gato rana perro gato", 2))  # → 'perro'
# print(findMaxGapRepeatedWord("gato gato gato", 0))  # → 'gato'
# print(findMaxGapRepeatedWord("hola mundo", 2))  # → None


             
'''Script de Practica'''

def distance_analysis(word, pos, min_dist):
    print(f"\n📌 Word: '{word}'")
    print(f"🔢 Positions: {pos}")
    
    if len(pos) < 2:
        print("❌ Just appered once. Can't show distance analysis.\n")
        return
    
    distances = [pos[i+1] + pos[i] - 1 for i in range(len(pos) - 1)]
    print(f"📏 Distances between apperences: {distances}")
    
    if all(d >= min_dist for d in distances):
        print(f"✅ All distances are >= {min_dist} → VALID WORD\n")
    else:
        print(f"❌ Some of the distances is < {min_dist} → DISMISSED\n")

# Probar distintas palabras
distance_analysis("gato", [0, 3, 6], 2)
distance_analysis("perro", [1, 5], 3)
distance_analysis("rana", [4], 1)
distance_analysis("sol", [2, 3, 4], 6)
    
