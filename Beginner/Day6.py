# Funcion que reciba una lista de pares [nombre,nota] y devuelva un diccionariodonde cada nombre tiene una lista de sus notas

# def group_notes(notes):
#     if not notes:
#         return None
    
#     grouped = {}
    
#     for name, note in notes:
#         if name not in grouped:
#             grouped[name] = []
        
#         grouped[name].append(note)
        
#     return grouped

# notes = [["Lalo", 9], ["Ana", 10], ["Lalo", 7], ["Luis", 8]]
# print(group_notes(notes))



# Ddo un arreglo con pares[nombre, nota], agrupa las notas por alumno y devuelve un diccionario con su promedio de calificaciones

# def student_avg(notes):
#     if not notes:
#         return None
    
#     avgs = {}
    
#     for name, note in notes:
#         if name not in avgs:
#             avgs[name] = [] 
#         avgs[name].append(note)
        
#     for name in avgs:
#         avgs[name] = sum(avgs[name]) / len(avgs[name])
        
#     return avgs
            
# notes = [
#     ["Lalo", 9], ["Ana", 10],
#     ["Lalo", 7], ["Luis", 8],
#     ["Ana", 9], ["Luis", 6]
# ]

# print(student_avg(notes))



#Crea una funcion que devuelva una lista con los nombres de los estudiantes cuyo promedio es mayor o igual a 9

# def top_students(notes):
#     if not notes:
#         return []
    
#     avgs = {}
#     res = []
    
#     for name, note in notes:
#         if name not in avgs:
#             avgs[name] = []
#         avgs[name].append(note)
            
#     for name in avgs:
#         avgs[name] = sum(avgs[name]) / len(avgs[name])
#         if avgs[name] >= 9:
#             res.append(name)
    
#     return res

# notes = [
#     ["Lalo", 9], ["Ana", 10],
#     ["Lalo", 7], ["Luis", 9],
#     ["Ana", 9]
# ]

# print(top_students(notes))
        

# Define una funcion que devuelva un numero entero: cuantos estudiantes  tienen al menos una nota de 6 o mas

# def count_passed_students(notes):
#     if not notes:
#         return 0
    
#     students = {}
#     count = 0
    
#     for name, note in notes:
#         if name not in students:
#             students[name] = []
#         students[name].append(note)
        
#     for name in students:
#         if any(n >= 6 for n in students[name]):
#             count += 1
            
#     return count

# notes = [
#     ["Lalo", 9], ["Ana", 5],
#     ["Lalo", 4], ["Luis", 8],
#     ["Ana", 3], ["Luis", 2]
# ]

# print(count_passed_students(notes))


#Escribe una funcion que reciba ina lista de pares y devuelva una tupla con el nombre del estudiante que tenga el promedio mas alta, junto a su promedio

# def best_student(notes):
#     if not notes:
#         return []
    
#     avgs = {}
#     max_avg = 0
#     top_students = []
    
#     for name, note in notes:
#         if name not in avgs:
#             avgs[name] = []
#         avgs[name].append(note)
        
#     for name in avgs:
#         avgs[name] = sum(avgs[name]) / len(avgs[name])
#         if max_avg < avgs[name]:
#             max_avg = avgs[name]
#             top_students = [name]
#         elif avgs[name] == max_avg:
#             top_students.append(name)
        
#     return (top_students, max_avg)

# notes = [
#     ["Lalo", 9], ["Ana", 10],
#     ["Lalo", 10], ["Ana", 9]
# ]
# print(best_student(notes))



#Estudiantes por rango de promedio, clasificar estudiantes en tres grupos segun su promedio

# def avg_range(notes):
#     if not notes:
#         return None
    
#     avgs = {}
    
#     for name, note in notes:
#         if name not in avgs:
#             avgs[name] = []
#         avgs[name].append(note)
    
    
#     students = {"Alto":[], "Medio":[], "Bajo":[]}
    
#     for name in avgs:
#         avg = sum(avgs[name]) / len(avgs[name])
        
#         if avg >= 9:
#             students["Alto"].append(name)
#         elif avg >= 6:
#             students["Medio"].append(name)
#         else:
#             students["Bajo"].append(name)
            
#     return students
    
# notes = [
#     ["Lalo", 9], ["Ana", 10],
#     ["Lalo", 7], ["Luis", 8],
#     ["Ana", 9], ["Luis", 2],
#     ["Karla", 5]
# ]

# print(avg_range(notes))


# Crear una funcion que reciba una lista de calificaciones y devuelva  un diccionario con la estructura designada:

def student_report(notes):
    if not notes:
        return None
    
    students = {}
    
    for name, note in notes:
        if name not in students:
            students[name] = []
        students[name].append(note)
        
    avgs = {"Promedios":{}, 
            "Aprobados":[], 
            "Reprobados":[], 
            "Mejores":[], 
            "Por_Rango":{"Alto":[], "Medio":[], "Bajo":[]}}
    
    max_avg = -1
     
    for name, grades in students.items():
        avg = sum(grades) / len(grades)
        avgs["Promedios"][name] = avg 
        
        if avg >= 9:
            avgs["Aprobados"].append(name)
            avgs["Por_Rango"]["Alto"].append(name)
        elif avg >= 6:
            avgs["Aprobados"].append(name)
            avgs["Por_Rango"]["Medio"].append(name)
        else:
            avgs["Reprobados"].append(name)
            avgs["Por_Rango"]["Bajo"].append(name)
            
        if avg > max_avg:
            max_avg = avg
            avgs["Mejores"] = [name]
        elif avg == max_avg:
            avgs["Mejores"].append(name)
            
    return avgs
            
         
notes = [
    ["Lalo", 9], ["Ana", 10],
    ["Lalo", 7], ["Luis", 8],
    ["Ana", 9], ["Luis", 2],
    ["Karla", 5]
]

print(student_report(notes))

