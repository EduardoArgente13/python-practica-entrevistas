'''
Dado un diccionario donde las llaves son nombres de cursos y los valores son conjuntos de estudiantes inscritos, 
devuelve un diccionario donde las llaves sean pares de estudiantes (en tuplas ordenadas alfabéticamente), 
y los valores sean los cursos que ambos comparten.
'''
# from collections import defaultdict
# from itertools import combinations

# def shared_by_2(courses):
#     if not courses:
#         return {}
    
#     shared_courses = defaultdict(set)
    
#     for course, students in courses.items():
#         for stu1, stu2 in combinations(students, 2):
#             pair = tuple(sorted((stu1, stu2)))
#             shared_courses[pair].add(course)
    
#     ordered = sorted(shared_courses.items(), key=lambda x: len(x[1]), reverse=True)
    
#     return ordered

# courses = {
#     'Python': {'Ana', 'Lalo', 'Beto'},
#     'Java': {'Lalo', 'Carlos'},
#     'SQL': {'Ana', 'Carlos'},
#     'C++': {'Ana', 'Carlos', 'Beto'}
# }

# for pair, shared in shared_by_2(courses):
#     print(f"{pair}: {shared}")



'''
Dado un diccionario courses donde la clave es el nombre del curso y el valor es un conjunto de estudiantes inscritos, determina para cada estudiante quién es la persona con la que más cursos comparte.
'''
# from collections import defaultdict
# from itertools import combinations

# def most_courses_together(courses):
#     if not courses:
#         return {}
    
#     shared_counts = defaultdict(int)
    
#     for group in courses.values():
#         for student1, student2 in combinations(group, 2):
#             pair = tuple(sorted((student1, student2)))
#             shared_counts[pair] += 1
    
#     student_relations = defaultdict(dict)
    
#     for (s1, s2), count in shared_counts.items():
#         student_relations[s1][s2] = count
#         student_relations[s2][s1] = count
    
#     res = {}
#     for student, relations in student_relations.items():
#         most_common = max(relations.items(), key=lambda x: x[1])[0]
#         res[student] = most_common
    
    
#     return res

# courses = {
#     "Math": ["Ana", "Beto", "Carlos"],
#     "Science": ["Ana", "Carlos"],
#     "English": ["Ana", "Diana"],
#     "History": ["Beto", "Carlos"],
# }

# print(most_courses_together(courses))


'''
📝 Enunciado:
Dado un diccionario llamado courses, 
donde cada clave es el nombre de un curso y su valor es una lista de estudiantes inscritos en ese curso, 
escribe una función que **devuelva una lista con los nombres de los estudiantes que están inscritos en exactamente un solo curso.
'''

# from collections import defaultdict

# def students_with_unique_courses(courses):
#     if not courses:
#         return []
    
#     students_courses = defaultdict(int)
    
#     for students in courses.values():
#         for student in students:
#             students_courses[student] += 1
    
#     res = []
#     for student, count in students_courses.items():
#         if count == 1:
#             res.append(student)
            
#     return res
        
# courses = {
#     "Math": ["Ana", "Beto", "Carlos"],
#     "Science": ["Ana", "Carlos"],
#     "English": ["Diana"],
#     "History": ["Emilia", "Carlos"],
# }

# print(students_with_unique_courses(courses))
      

'''
Dado un conjunto de estudiantes y un diccionario de cursos donde cada curso tiene una lista de estudiantes inscritos, escribe una función que devuelva la lista de estudiantes que no están inscritos en ningún curso.
'''

def students_with_no_courses(all_students, courses):
    if not all_students:
        return []
    
    enrolled_students = set()
    for student_list in courses.values():
        enrolled_students.update(student_list)
        
    res = []
    for student in all_students:
        if student not in enrolled_students:
            res.append(student)
            
    return res
    
    
all_students = ["Ana", "Beto", "Carlos", "Diana", "Emilia"]

courses = {
    "Math": ["Ana", "Carlos"],
    "Science": ["Ana"],
    "English": ["Diana"],
}

print(students_with_no_courses(all_students, courses))

    
