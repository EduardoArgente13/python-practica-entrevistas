'''
Ordena a los empleados por su area de trabajo
'''

# def order_employees(employees):
#     if not employees:
#         return {}
    
#     res = {}
    
#     for employee in employees:
#         area = employee[1]
#         name = employee[0]
        
#         if area not in res:
#             res[area] = []
#         res[area].append(name)
        
#     return res

# employees = [
#     ('Lalo', 'TI'),
#     ('Ana', 'Ventas'),
#     ('Carlos', 'TI'),
#     ('Luis', 'Recursos Humanos'),
#     ('María', 'Ventas')
# ]

# print(order_employees(employees))

'''Variante'''

# from collections import defaultdict

# def order_employees(employees):
#     res = defaultdict(set)
#     for name, area in employees:
#         res[area].add(name)
#     return dict(res)


'''Conteo (Counter)'''

# from collections import Counter

# words = ['python', 'java', 'python', 'c++', 'java', 'python']

# count = Counter(words)
        
# print(dict(count))

'''Contar Frutas'''

# def count_fruits(fruits):
#     if not fruits:
#         return {}
    
#     res = {}
    
#     for fruit in fruits:
#         res[fruit] = res.get(fruit, 0) + 1
        
#     return res

# #

# from collections import Counter

# def count_fruits_counter(fruits):
#     if not fruits:
#         return {}
    
#     res = Counter(fruits)
        
#     return dict(res)
        
'''
Dado un string cualquiera, escribe una función que cuente la frecuencia de cada letra, 
ignorando espacios y sin distinguir entre mayúsculas y minúsculas.
'''

# def letter_frequency(string):
#     if not string:
#         return {}
    
#     res = {}
    
#     for char in string.lower():
#         if char
#         string[char] = string.get(char, 0) + 1
        
#     return res

# # Variante

# from collections import Counter

# def letter_frequency_counter(text):
#     text = text.lower().replace(" ", "")
#     return dict(Counter(text))



'''
Objetivos:
✅ Crear un diccionario que agrupe a los alumnos por curso (sin duplicados).

✅ Mostrar cuántos alumnos únicos hay en cada curso.
'''

from collections import defaultdict, Counter

def courses(signatures):
    if not signatures:
        return {}
    
    res = defaultdict(set)
    for name, topic in signatures:
        res[topic].add(name)
    
    count = {course: len(students) for course, students in res.items()}
    
    return dict(res), count
        



