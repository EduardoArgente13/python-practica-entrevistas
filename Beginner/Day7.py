# Dada una lista, cre un conjunto con las palabras unicas y convierte ese conjunto de nuevoi a una lista ordenada alfabeticamente

# def no_duplicates(words):
#     if not words:
#         return []
    
#     uniques = set(words)
#     res = []
    
#     for word in uniques:
#         res.append(word)
        
#     sorted_res = sorted(res)
        
#     return sorted_res

# words = ["gato", "perro", "gato", "ratón", "perro", "pato"]
# print(no_duplicates(words))

#Variante

# def no_duplicates(words):
#     return sorted(set(words))


#Dada una lista de tuplas, imprime cada nombre con su edad y encuentra la persdona de mayor edad

# def fixed_data_record(records):
#     if not records:
#         return None
    
#     max_age = 0
#     max_age_name = ""
    
#     for name, age in records:
#         print(name, age)
#         if age > max_age:
#             max_age = age
#             max_age_name = name
    
#     ans = (f"{max_age_name} is the oldest at {max_age} years old.")
#     return ans

# records = [
#     ("Carlos", 23),
#     ("Ana", 25),
#     ("Luis", 21)
# ]

# print(fixed_data_record(records))

# #Variante
# def fixed_data_record(records):
#     if not records:
#         return None
    
#     for name, age in records:
#         print (name, age)
        
#     oldest = max(records, key=lambda x: x[1])
#     return f"{oldest[0]} is the oldest at {oldest[1]} years old."


#Dada una lista de ciudadades y coordenadas, elimina registros duplicados (Ciudad y coordenadas iguales),
#convierte el resultado en un diccionario donde la clave sea la ciudad y el calor la coordenada y muestra las ciudaddes ordenadas alfabeticamente con sus coordenadas

# def location_records_analysis(cities):
#     if not cities:
#         return {}
    
#     unique_records = set(cities)
#     res = {}
    
#     for city, coord in sorted(unique_records):
#         if city not in res:
#             res[city] = coord
            
#     return res

# cities = [
#     ("CDMX", (19.4326, -99.1332)),
#     ("Guadalajara", (20.6597, -103.3496)),
#     ("Monterrey", (25.6866, -100.3161)),
#     ("CDMX", (19.4326, -99.1332)),  # repetido
#     ("Querétaro", (20.5888, -100.3899))
# ]

# print(location_records_analysis(cities))


# Dada una lista de logs, contar cuantas veces accedio cada usuario, mostrar para cada usuario las ciudades distintas desde donde accedio
# y detectar usuarios que accedieron dede mas de 2 ciudades distintas

# def count_user_accesses(logs):
#     if not logs:
#         return {}
    
#     user_counts = {}
#     user_cities = {}
#     res = []
    
#     for user, city in logs:
#         user_counts[user] = user_counts.get(user, 0) + 1
#         if user not in user_cities:
#             user_cities[user] = set()
#         user_cities[user].add(city)
        
#     for user, cities in user_cities.items():
#         if len(cities) > 2:
#             res.append(user)
        
#     return user_counts, user_cities, res

# logs = [
#     ("Eduardo", "CDMX"),
#     ("Ana", "Querétaro"),
#     ("Luis", "CDMX"),
#     ("Eduardo", "Guadalajara"),
#     ("Ana", "Querétaro"),
#     ("Luis", "CDMX"),
#     ("Luis", "Monterrey"),
#     ("Eduardo", "CDMX"),
#     ("Eduardo", "Monterrey")  # <-- ahora sí Eduardo tiene 3 ciudades
# ]

# counts, cities, multi_city_users = count_user_accesses(logs)

# print("Accesos:", counts)
# print("Ciudades únicas:", cities)
# print("Usuarios con más de 2 ciudades:", multi_city_users)


#Contar cuántas reacciones hizo cada usuario en total, Listar los tipos de reacciones únicas que hizo cada usuario
#Detectar usuarios que reaccionaron a más de 2 publicaciones distintas, Evitar contar reacciones duplicadas

# def reaction_analysis(reactions):
#     if not reactions:
#         return None
    
#     user_react_count = {}
#     user_react_types = {}
#     user_post_ids = {}
#     unique_reactions = set()
#     res = []
    
#     for react, user, post in reactions:
#         key = (user, react, post)
#         if key in unique_reactions:
#             continue #Evitar Duplicados
#         unique_reactions.add(key)
        
#         #Conteo Total
#         user_react_count[user] = user_react_count.get(user, 0) + 1
        
#         #Tipos de Reaccion
#         if user not in user_react_types:
#             user_react_types[user] = set()
#         user_react_types[user].add(react)
        
#         #Post Unicos
#         if user not in user_post_ids:
#             user_post_ids[user] = set()
#         user_post_ids[user].add(post)
        
#     #Detectar usuarios que reaccionaron a mas de 2 posts
#     for user, posts in user_post_ids.items():
#         if len(posts) > 2:
#             res.append(user)
            
#     return user_react_count, user_react_types, res
    
# reactions = [
#     ("like", "Ana", 101),
#     ("love", "Luis", 101),
#     ("like", "Ana", 102),
#     ("like", "Carlos", 101),
#     ("haha", "Ana", 103),
#     ("like", "Luis", 101),
#     ("like", "Luis", 104),
#     ("love", "Carlos", 102),
#     ("haha", "Carlos", 101),
#     ("like", "Ana", 101),  # repetida
# ]

# count, types, multiple_posts = reaction_analysis(reactions)
# print("Reacciones por usuario:", count)
# print("Tipos de reacciones por usuario:", types)
# print("Usuarios con más de 2 posts:", multiple_posts)


