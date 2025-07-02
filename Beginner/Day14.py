'''
Problema:
Dado un arreglo de enteros nums, devuelve True si existen dos números distintos tales que:

Su suma sea igual a un número objetivo target

La diferencia entre sus índices sea como máximo k
'''

# def twosum(nums, target, k):
#     if not nums:
#         return False
    
#     num_map = {}
    
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in num_map:
#             j = num_map[complement]
#             if abs(i - j) <= k:
#                 return True
#         num_map[num] = i
        
#     return False

# print(twosum([1, 3, 5, 7, 9], 10, 2))  # True (3 + 7, dist = 2)
# print(twosum([1, 2, 3, 4, 5], 9, 1))   # False (4 + 5 = 9 pero distancia > 1)
# print(twosum([], 7, 1))               # False


'''
 Ejercicio 2: Contar pares con suma objetivo
Dado un arreglo de enteros nums y un entero target, encuentra cuántos pares distintos (i, j) existen tal que:

nums[i] + nums[j] == target

i < j
'''
# from collections import Counter

# def pair_sums_target(nums, target):
#     if not nums:
#         return 0
    
#     count = Counter(nums)
#     seen = set()
#     total_pairs = 0
    
    
#     for num in count:
#         complement =  target - num
        
#         if complement in count and (complement, num) not in seen and (num, complement) not in seen:
#             if complement != num:
#                 total_pairs += count[num] * count[complement]
#             else:
#                 total_pairs += count[num] * (count[num] - 1) // 2
#             seen.add((num, complement))
            
#     return total_pairs

# nums = [1, 3, 2, 2, 4, 5]
# target = 5

# print(pair_sums_target(nums, target))  # Output esperado: 3



'''
Problema:
Dado un arreglo de enteros nums y un entero k, determina si existen dos índices distintos i y j tales que:

nums[i] == nums[j]

abs(i - j) <= k
'''

# def contains_nearby_duplicate(nums, k):
#     if not nums:
#         return False
    
#     num_indexes = {}
    
#     for i, num in enumerate(nums):
#         if num in num_indexes:
#             prev_index = num_indexes[num]
#             if i - prev_index <= k:
#                 return True
#         num_indexes[num] = i
    
#     return False
    
# print(contains_nearby_duplicate([1, 2, 3, 1], 3))  # ✅ True
# print(contains_nearby_duplicate([1, 0, 1, 1], 1))  # ✅ True
# print(contains_nearby_duplicate([1, 2, 3, 4], 1))  # ❌ False

    
'''
💡 Problema: containsNearbyAlmostDuplicate(nums, k, t)
Dado un arreglo de enteros nums, y dos enteros k y t, determina si existen dos índices i y j tales que:

abs(i - j) <= k ← Índices cercanos

abs(nums[i] - nums[j]) <= t ← Valores también cercanos
''' 

# import bisect

# def contains_nearby_almost_duplicate(nums, k, t):
#     if t < 0 or k <= 0:
#         return False
    
#     window = []
    
#     for i, num in enumerate(nums):
#         pos = bisect.bisect_left(window, num - t)
        
#         if pos < len(window) and abs(window[pos] - num) <= t:
#             return True
        
#         bisect.insort(window, num)
        
#         if len(window) > k:
#             del_idx = bisect.bisect_left(window, nums[i - k])
#             window.pop(del_idx)
            
#     return False

# print(contains_nearby_almost_duplicate([1, 2, 3, 1], 3, 0))  # ✅ True
# print(contains_nearby_almost_duplicate([1, 0, 1, 1], 1, 2))  # ✅ True
# print(contains_nearby_almost_duplicate([1, 5, 9, 1, 5, 9], 2, 3))  # ❌ False


'''
Problema: contains_nearby_duplicate(nums, k)
📜 Enunciado:
Dado un arreglo de enteros nums y un entero k,
verifica si existen dos elementos iguales dentro de una ventana de longitud k.

Es decir, si nums[i] == nums[j] y |i - j| <= k
'''

def contains_nearby_duplicate(nums, k):
    if not nums:
        return False
    
    seen = set()
    
    for i, num in enumerate(nums):
        
        if num in seen:
            return True
        
        seen.add(num)
        
        if len(seen) > k:
            seen.remove(nums[i - k])
            
    return False

print(contains_nearby_duplicate([1, 2, 3, 1], 3))  # ✅ True
print(contains_nearby_duplicate([1, 2, 3, 4, 5], 2))  # ❌ False
print(contains_nearby_duplicate([1, 0, 1, 1], 1))  # ✅ True

