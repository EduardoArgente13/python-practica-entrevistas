# Agrupar elementos  con diccionarios y sets

# def count_access(logs):
#     access = {}
#     for user in logs:
#         access[user] = access.get(user, 0) + 1
        
#     return access


# Agrupar ciudades por usuario

# def cities_by_user(logs):
#     grouped = {}
#     for user, city in grouped:
#         if user not in grouped:
#             grouped[user] = set()
#         grouped[user].add(city)
#     return grouped


# Analizar ventas

# def sales_analysis(sales):
#     if not sales:
#         return []
    
#     totals = {}
#     products = {}
#     cities = {}
    
#     for client, prod, city, amount in sales:
#         totals[client] = totals.get(client, 0) + amount
#         if client not in products:
#             products[client] = set()
#         products[client].add(prod)
#         if client not in cities:
#             cities[client] = set()
#         cities[client].add(city)
        
#     return totals, products, cities

# #Filtros finales

# def client_filters(totals, products, cities):
#     selected = []
#     for client in totals:
#         if totals[client] > 30 and len(products[client]) > 2 and len(cities[client]) > 1:
#             selected.append(client)
#     return sorted(selected)


'''Escribe una función review_analysis(reviews) que devuelva:

-Un diccionario con el total de puntos acumulados por cada usuario (solo reseñas aprobadas).

-Un diccionario con el set de películas que cada usuario ha reseñado.

-Una lista de usuarios que:

-Hayan hecho reseñas aprobadas en más de una ciudad.

Y hayan reseñado más de 2 películas distintas.
'''

# def review_analysis(reviews):
#     if not reviews:
#         return {}
    
#     total_scores = {}
#     user_movies = {}
#     user_cities = {}
#     approved_users = set()
    
#     for user, movie, city, score, status in reviews:
#         if status != "aprobada":
#             continue
        
#         total_scores[user] = total_scores.get(user, 0) + score
        
#         if user not in user_movies:
#             user_movies[user] = set()
#         user_movies[user].add(movie)
        
#         if user not in user_cities:
#             user_cities[user] = set()
#         user_cities[user].add(city)
    
#     for user in total_scores:
#         if len(user_cities[user]) > 1 and len(user_movies[user]) > 2:
#             approved_users.add(user)
    
#     return total_scores, user_movies, approved_users
        
# reviews = [
#     ("Ana", "Matrix", "CDMX", 5, "aprobada"),
#     ("Ana", "Inception", "CDMX", 4, "aprobada"),
#     ("Ana", "Interstellar", "Guadalajara", 5, "aprobada"),
#     ("Luis", "Matrix", "Monterrey", 3, "rechazada"),
#     ("Luis", "Matrix", "Monterrey", 4, "aprobada"),
#     ("Luis", "Inception", "Monterrey", 5, "aprobada"),
#     ("Sofi", "Matrix", "CDMX", 5, "aprobada"),
#     ("Sofi", "Inception", "CDMX", 5, "rechazada")
# ]

# print(review_analysis(reviews))



# Crea un diccionario total_spent con el total gastado por cada usurio solo si el estado es "pagado"

# def concert_analysis(attendances):
#     if not attendances:
#         return {}
    
#     total_spent = {}
#     user_artists = {}
#     user_cities = {}
#     cancelled_users = set()
#     fans = set()
    
#     for attendance in attendances:
#         user, artist, city, price, status = attendance
        
#         if status == "canceled":
#             cancelled_users.add(user)
#             continue
        
#         total_spent[user] = total_spent.get(user, 0) + price
        
#         if user not in user_artists:
#             user_artists[user] = set()
#         user_artists[user].add(artist)
        
#         if user not in user_cities:
#             user_cities[user] = set()
#         user_cities[user].add(city)
        
#     for user in total_spent:
#         if len(user_artists[user]) > 2 and len(user_cities[user]) > 1 and user not in cancelled_users:
#             fans.add(user)
            
        
#     return {'total': total_spent, 'artistas': user_artists, 'ciudades': user_cities, 'fans': fans}
        


#Analisis de usuarios activos en plataformas de streaming

# def active_users_analysis(logs):
#     if not logs:
#         return {}
    
#     total_time = {}
#     platforms = {}
#     cities = {}
#     super_users = set()
    
#     for log in logs :
#         user, platform, city, time, status = log
        
#         if status != "active":
#             continue
        
#         total_time[user] = total_time.get(user, 0) + time
#         platforms.setdefault(user, set()).add(platform)
#         cities.setdefault(user, set()).add(city)
        
#     for user in total_time:
#         if len(platforms[user]) > 2 and len(cities[user]) > 1:
#             super_users.add(user)
            
#     return {'total time': total_time, 'platforms': platforms, 'cities': cities, 'super_users': super_users}
            
    
# '''Dado un listado de ventas con registros (cliente, producto, cantidad, precio_unitario), calcula:

# El total gastado por cada cliente (cantidad × precio_unitario)

# Devuelve un diccionario {cliente: total_gastado} ordenado de mayor a menor gasto'''
 

# def total_spent_per_client(sales):
#     if not sales:
#         return {}
    
#     total_spent = {}
    
#     for sale in sales:
#         client, product, quantity, price = sale
        
#         total_spent[client] = total_spent.get(client, 0) + (quantity * price)
        
#     sorted_totals = dict(sorted(total_spent.items(), key=lambda item: item[1], reverse=True))
    
#     return sorted_totals

# sales = [
#     ("Ana", "Camisa", 2, 300),
#     ("Luis", "Pantalón", 1, 500),
#     ("Ana", "Zapatos", 1, 700),
#     ("Luis", "Camisa", 3, 300),
# ]

# print(total_spent_per_client(sales))