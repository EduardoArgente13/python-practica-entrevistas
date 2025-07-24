'''
🧩 Ejercicio 1: Invertir agrupamiento
Tienes un diccionario como este (ya agrupado por curso):
cursos = {
    'Python': {'Lalo', 'Ana'},
    'Java': {'Lalo', 'Carlos'},
    'C++': {'Ana'}
}
🎯 Reto: Invierte esta estructura para obtener un diccionario que muestre qué cursos tiene cada persona:
'''
# from collections import defaultdict

# def invert_dict(courses):
#     if not courses:
#         return {}
    
#     students = defaultdict(set)
    
#     for course, group in courses.items():  # 'group' es el set de estudiantes
#         for student in group:  # ahora sí recorremos cada estudiante en el set
#             students[student].add(course)
            
#     return dict(students)


# cursos = {
#     'Python': {'Lalo', 'Ana'},
#     'Java': {'Lalo', 'Carlos'},
#     'C++': {'Ana'}
# }

# resultado = invert_dict(cursos)
# print(resultado)


'''
Quién Comparte Cursos con Quién
Dado un diccionario de cursos y estudiantes (como el de antes),
escribe una función que devuelva un diccionario donde cada persona tenga una lista de personas con las que comparte al menos un curso.
'''

# from collections import defaultdict

# def shared_courses(courses):
#     if not courses:
#         return {}
    
#     shared = defaultdict(set)
    
#     for course, group in courses.items():
#         for student in group:
#             others = group - {student}
#             shared[student].update(others)
    
#     return dict(shared)

# # Prueba
# courses = {
#     'Python': {'Lalo', 'Ana'},
#     'Java': {'Lalo', 'Carlos'},
#     'C++': {'Ana', 'Carlos'}
# }

# res = shared_courses(courses)
# print(res)
    

'''
Queremos construir una función que reciba una lista de tuplas con el formato:
[
    ('Lalo', 'Python'),
    ('Ana', 'Python'),
    ('Lalo', 'Java'),
    ('Carlos', 'Java'),
    ('Carlos', 'C++'),
    ('Ana', 'C++')
]
Y que devuelva un diccionario con pares de estudiantes que comparten al menos un curso, indicando cuántos cursos comparten.
'''
from collections import defaultdict, Counter
from itertools import combinations

def group_by_course(data):
    res = defaultdict(set)
    for student, course in data:
        res[course].add(student)
    return dict(res)

def count_shared_courses(courses):
    shared = Counter()
    for students in courses.values():
        for pair in combinations(sorted(students), 2):
            shared[pair] += 1
    return dict(shared)

def print_shared_courses(shared):
    if not shared:
        print("No hay estudiantes que compartan cursos.")
        return
    for (a, b), count in sorted(shared.items()):
        print(f"{a} y {b} comparten {count} curso(s).")

# Datos de ejemplo
data = [
    ('Lalo', 'Python'),
    ('Ana', 'Python'),
    ('Lalo', 'Java'),
    ('Carlos', 'Java'),
    ('Carlos', 'C++'),
    ('Ana', 'C++')
]

grouped = group_by_course(data)
shared = count_shared_courses(grouped)
print_shared_courses(shared)
    
    
    

