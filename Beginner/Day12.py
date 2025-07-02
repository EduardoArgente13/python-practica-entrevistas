'''Cada registro contiene información de una visita al gimnasio:

python
Copiar código
(visita_id, cliente, sucursal, clase_tomada, duración_minutos, estado)
estado: puede ser 'completada', 'cancelada', 'incompleta'.

🎯 Objetivos:
Calcular el tiempo total ejercitado por cliente (solo clases completadas).

Registrar clases distintas tomadas por cada cliente.

Contabilizar sucursales diferentes visitadas por cliente.

Identificar a los clientes activos: aquellos que tengan más de 150 minutos de ejercicio, al menos 2 clases diferentes y hayan ido a más de 1 sucursal.

Excluir de los clientes activos a los que tengan más de 2 visitas canceladas.
'''

# def gym_membership_analysis(memberships):
#     if not memberships:
#         return {}
    
#     total_time = {}
#     client_classes = {}
#     client_gyms = {}
#     canceled_visits = {}
    
#     for membership in memberships:
#         visit_id, client, gym, class_taken, minutes, status = membership
        
#         if status == 'cancelada':
#             canceled_visits[client] = canceled_visits.get(client, 0) + 1
#             continue
        
#         if status != 'completada':
#             continue
        
#         total_time[client] = total_time.get(client, 0) + minutes
#         client_classes.setdefault(client, set()).add(class_taken)
#         client_gyms.setdefault(client, set()).add(gym)
        
#     active_clients = set()
#     for client in total_time:
#         if total_time[client] > 150 and len(client_classes[client]) >= 2 and len(client_gyms[client]) > 1 and canceled_visits.get(client, 0) <= 2:
#             active_clients.add(client)
            
#     return {
#         "total_time": total_time,
#         "client_classes": client_classes,
#         "client_gyms": client_gyms,
#         "active_clients": active_clients
#     }

# memberships = [
#     (1, "Ana", "GymPlus", "Yoga", 60, "completada"),
#     (2, "Ana", "PowerFit", "Spinning", 45, "completada"),
#     (3, "Ana", "GymPlus", "Cardio", 60, "completada"),
#     (4, "Luis", "PowerFit", "Yoga", 30, "cancelada"),
#     (5, "Luis", "PowerFit", "Spinning", 30, "cancelada"),
#     (6, "Luis", "PowerFit", "Spinning", 30, "cancelada"),
#     (7, "Sofi", "EnergyZone", "Yoga", 80, "completada"),
#     (8, "Sofi", "EnergyZone", "Spinning", 80, "completada"),
#     (9, "Sofi", "FitClub", "Cardio", 30, "completada"),
#     (10, "Tom", "FitClub", "Yoga", 100, "completada"),
#     (11, "Tom", "FitClub", "Spinning", 60, "completada"),
#     (12, "Tom", "FitClub", "Yoga", 60, "completada"),
# ]

# resultado = gym_membership_analysis(memberships)

# from pprint import pprint
# pprint(resultado)

    

'''
Escribe una función course_participation_analysis(courses) que reciba una lista de tuplas con esta estructura:

python
Copiar código
(curso_id, estudiante, curso, categoría, horas, estado)
curso_id: ID único de la participación

estudiante: nombre del estudiante

curso: nombre del curso

categoría: ciencia, arte, negocios, etc.

horas: cantidad de horas completadas

estado: "completado" o "abandonado"
'''

def onlinecourses_analysis(courses):
    if not courses:
        return {}
    
    total_hours = {}
    student_courses = {}
    student_categories = {}
    abandoned_courses = {}
    outstandings = []
    specialists = []
    
    for course in courses:
        course_id, student, course, category, hours, status = course
        
        if status == 'abandoned':
            abandoned_courses[student] = abandoned_courses.get(student, 0) + 1
            continue
        
        if status != 'completed':
            continue
        
        total_hours[student] = total_hours.get(student, 0) + hours
        student_courses.setdefault(student, set()).add(course)
        student_categories.setdefault(student, set()).add(category)
    
    for student in total_hours:
        num_courses = len(student_courses[student])
        avg_hours = total_hours[student] / num_courses
        abandoned = abandoned_courses.get(student, 0)
        
        if total_hours[student] > 150 and num_courses >= 4 and len(student_categories[student]) >= 2 and abandoned < 2 and avg_hours >= 40:
            outstandings.append(student)
        if any(list(student_categories[student]).count(cat) > 3 for cat in student_categories[student]):
            specialists.append(student)
                  
    return {
        "total_hours": total_hours,
        "student_courses": student_courses,
        "student_categories": student_categories,
        "abandoned_courses": abandoned_courses,
        "outstandings": outstandings,
        "specialists": specialists
    }
        
courses = [
    (1, "Ana", "Python", "Tecnología", 50, "completed"),
    (2, "Ana", "Dibujo", "Arte", 40, "completed"),
    (3, "Ana", "Historia del Arte", "Arte", 30, "completed"),
    (4, "Ana", "SQL", "Tecnología", 60, "completed"),
    (5, "Ana", "UX", "Diseño", 20, "abandoned"),
    
    (6, "Luis", "Negocios 101", "Negocios", 60, "completed"),
    (7, "Luis", "Contabilidad", "Negocios", 50, "abandoned"),
    (8, "Luis", "Marketing", "Negocios", 55, "completed"),
    (9, "Luis", "Ventas", "Negocios", 40, "completed"),

    (10, "Sofi", "Inglés", "Idiomas", 80, "completed"),
    (11, "Sofi", "Francés", "Idiomas", 90, "completed"),
    (12, "Sofi", "Italiano", "Idiomas", 100, "completed"),
    (13, "Sofi", "SQL", "Tecnología", 110, "completed"),
    (14, "Sofi", "Arte Digital", "Arte", 60, "completed"),
]

print(onlinecourses_analysis(courses))

