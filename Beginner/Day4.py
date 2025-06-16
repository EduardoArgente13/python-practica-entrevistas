# Dado un string, encuentra el caracter que mas veces aparece

# def mostFrequentChar(s):
#     if not s:
#         return None
    
#     seen = {}
#     most_freq = ""
#     max_count = 0
    
#     for char in s:
#         seen[char] = seen.get(char, 0) + 1
        
#     for value, count in seen.items():
#         if count > max_count:
#             max_count = count
#             most_freq = value
        
#     return (most_freq, max_count)

# print(mostFrequentChar("banana"))


#Dada una cade s, encuentra el primer caracter no repetido y retorna su indice. Si todo los caracteres se repiten regresa -1

# def first_unique_char(s):
#     if not s:
#         return -1

#     seen = {}
    
#     for char in s:
#         seen[char] = seen.get(char, 0) + 1

#     for i, char in enumerate(s):
#         if seen[char] == 1:
#             return i
        
#     return -1

# print(first_unique_char("leetcode"))       # 0
# print(first_unique_char("loveleetcode"))   # 2
# print(first_unique_char("aabb"))           # -1



# Dada una lista de palabras, encuetra todas las palabras que no se repiten y preservalas en orden

# def unique_words(strs):
#     if not strs:
#         return []
    
#     seen = {}
#     for word in strs:
#         seen[word] = seen.get(word, 0) + 1
    
#     res = []
#     for word in strs:
#         if seen[word] == 1:
#             res.append(word)
            
#     return res

# print(unique_words(["apple", "banana", "apple", "cherry", "banana", "durian"]))


# Validar si los parentesis en una cade estan balanceados y bien cerrdos

# def is_valid_parenthesis(s):
#     stack = []
#     mapping = {')':'(', ']':'[', '}':'{'}
    
#     for char in s:
#         if char in mapping.values():
#             stack.append(char)
#         elif char in mapping:
#             if not stack or stack.pop() != mapping[char]:
#                 return False
#     return not stack


# Escribe una función que verifique si una cadena de solo paréntesis ()[]{} está bien balanceada

# def isBalanced(s):
#     if not str:
#         return False
    
#     stack = []
#     mapping = {')':'(', ']':'[', '}':'{'}
    
#     for char in s:
#         if char in mapping.values():
#             stack.append(char)
#         elif char in mapping:
#             if not stack or stack[-1] != mapping[char]:
#                 return False
#             stack.pop()
#         else:
#             continue
    
#     return not stack

# print(isBalanced("([]{})"))   # ✅ True
# print(isBalanced("([)]"))     # ❌ False
# print(isBalanced("{[()]}"))   # ✅ True
# print(isBalanced("((("))      # ❌ False
# print(isBalanced(""))         # ✅ True (según convención)


# Dado un string s que contiene letras y paréntesis '(' y ')', elimina el mínimo número de paréntesis para que la cadena sea válida (balanceada). Devuelve el string resultante.

# def minRemoveToMakeValid(s):
#     if not s:
#         return ""
    
#     s = list(s)
#     stack = []
    
#     for i, char in enumerate(s):
#         if char == '(':
#             stack.append(i)
#         elif char == ')':
#             if stack:
#                 stack.pop()
#             else:
#                 s[i] = ''
    
#     for i in stack:
#         s[i] = ''

#     return ''.join(s)

# print(minRemoveToMakeValid("a)b(c)d"))      # ab(c)d
# print(minRemoveToMakeValid("))(("))         # ""
# print(minRemoveToMakeValid("(a(b(c)d)"))    # a(b(c)d)

