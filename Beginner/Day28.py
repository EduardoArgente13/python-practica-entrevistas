'''
Objetivo:
Construir un diccionario donde la clave sea una tupla de dos estudiantes y el valor sea el número de cursos que comparten.
'''
# from collections import defaultdict
# from itertools import combinations

# def order_courses_by_student_pairs(courses):
#     if not courses:
#         return {}
    
#     shared = defaultdict(int)
    
#     for group in courses.values():
#         for student1, student2 in combinations(group, 2):
#             pair = tuple(sorted((student1, student2)))
#             shared[pair] += 1
            
#     ordered = sorted(shared.items(), key=lambda x: x[1], reverse=True)
    
#     return ordered

# courses = {
#     'Python': {'Lalo', 'Ana'},
#     'Java': {'Lalo', 'Carlos'},
#     'C++': {'Ana', 'Carlos', 'Lalo'}
# }

# resultado = order_courses_by_student_pairs(courses)
# for pair, count in resultado:
#     print(f"{pair[0]} y {pair[1]} comparten {count} curso(s).")



'''
🎯 Objetivo
A partir de un diccionario que relaciona cursos con estudiantes, encuentra los estudiantes que comparten exactamente el mismo conjunto de cursos.
'''

# from collections import defaultdict

# def same_number_of_courses(courses):
#     if not courses:
#         return {}
    
#     student_courses = defaultdict(set)
    
#     for course, students in courses.items():
#         for student in students:
#             student_courses[student].add(course)
            
#     grouped = defaultdict(set)
    
#     for student, course_set in student_courses.items():
#         grouped[frozenset(course_set)].add(student)
    
#     return dict(grouped)

# courses = {
#     'Python': {'Ana', 'Lalo'},
#     'Java': {'Lalo', 'Carlos'},
#     'C++': {'Ana', 'Carlos'},
#     'SQL': {'Carlos'},
# }

# resultado = same_number_of_courses(courses)
# for key, value in resultado.items():
#     print(f"{set(key)}: {value}")



'''
Crea una función que devuelva una lista con el o los estudiantes que toman más cursos, y cuántos cursos toma cada uno.
'''

# from collections import defaultdict

# def top_students_by_courses(courses):
#     if not courses:
#         return []
    
#     res = defaultdict(set)

#     for course, students in courses.items():
#         for student in students:
#             res[student].add(course)
    
#     max_count = max(len(cursos) for cursos in res.values())
#     top = [(student, len(cursos)) for student, cursos in res.items() if len(cursos) == max_count]
#     return top

            
# courses = {
#     'Python': {'Ana', 'Lalo'},
#     'Java': {'Lalo', 'Carlos'},
#     'C++': {'Ana', 'Carlos'},
#     'SQL': {'Carlos'},
# }

# print(top_students_by_courses(courses))


'''
Dado un diccionario con cursos como claves y conjuntos de estudiantes como valores, devuelve una lista de estudiantes que solo están inscritos en un solo curso.
'''

from collections import defaultdict

def students_in_one_course(courses):
    if not courses:
        return []
    
    students_courses = defaultdict(set)
    
    for course, students in courses.items():
        for student in students:
            students_courses[student].add(course)
    
    sort = [student for student, cset in students_courses.items() if len(cset) == 1]
            
    return sort



        
    
    
    





