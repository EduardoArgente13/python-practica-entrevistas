#Dado un arreglo de enteros regresa el numero que mas aparece y cuantas veces aparece
# def mostRepeated(nums):
#     if not nums:
#         return None
    
#     seen = {}
    
#     for num in nums:
#         seen[num] = seen.get(num, 0) + 1
    
#     most_repeated = None
#     max_count = 0
    
#     for value, count in seen.items():
#         if count > max_count:
#             max_count = count
#             most_repeated = value
            
#     print(f"El valor mas repetido es: {most_repeated}")
#     print(f"Se repite: {max_count} veces")

# nums = [1, 1, 2, 3, 2, 1, 4, 2, 2]
# print(mostRepeated(nums))

# Dado un arreglo de enteros regresa LOS NUMEROS que mas se repiten y la frequencia, si son mas de uno o solo 1
# def mostRepeatedNums(nums):
#     if not nums:
#         return None
#     seen = {}
    
#     for num in nums:
#         seen[num] = seen.get(num, 0) + 1
        
#     repeated = []
#     max_count = 0
    
#     for value, count in seen.items():
#         if count > max_count:
#             max_count = count
#             repeated = [value]
#         elif count == max_count:
#             repeated.append(value)
        
#     return (repeated, max_count)


# nums = [1, 2, 2, 3, 3, 4, 4, 4]
# print(mostRepeatedNums(nums))


#Dado un arreglo de enteros nums y un entero k, devuelve los k elementos mas frecuentes en el arreglo. El orden no importa
# def topKFrequent(nums, k):
#     if not nums or k <= 0:
#         return []

#     seen = {}
#     for num in nums:
#         seen[num] = seen.get(num, 0) + 1

#     # Ordenamos las tuplas por frecuencia descendente
#     sorted_items = sorted(seen.items(), key=lambda x: x[1], reverse=True)

#     # Devolvemos solo los k valores más frecuentes
#     return [item[0] for item in sorted_items[:k]]


# print(topKFrequent([1, 1, 1, 2, 2, 3], 2))  # Output esperado: [1, 2]


#Group Anagrams: Dado un arreglo de string, agrupalos en grupos de anagramas

# def groupAnagrams(strs):
#     if not strs:
#         return []
    
#     seen = {}
    
#     for word in strs:
#         key = ''.join(sorted(word))
#         if key not in seen:
#             seen[key] = []
#         seen[key].append(word)
        
#     return list(seen.values())
    
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(groupAnagrams(strs))        
