'''
Objetivos:
Calcular:

Total de likes y comentarios por usuario ✅

Cantidad de publicaciones por tipo y por plataforma usando Counter ✅

Plataformas únicas por usuario (con defaultdict(set)) ✅

Detectar:

Usuarios con más de 500 likes y al menos 2 plataformas distintas → agregarlos a influencers ✅
'''
# from collections import Counter, defaultdict

# def post_engagement_analysis(posts):
#     if not posts:
#         return {}
    
#     total_likes = defaultdict(int)
#     total_comments = defaultdict(int)
#     type_counter = Counter()
#     platform_counter = Counter()
#     user_platforms = defaultdict(set)
#     influencers = []
    
#     for post in posts:
#         user, platform, post_type, likes, comments = post
#         total_likes[user] += likes
#         total_comments[user] += comments
        
#         type_counter[post_type] += 1
#         platform_counter[platform] += 1
        
#         user_platforms[user].add(platform)
        
#     for user in total_likes:
#         if total_likes[user] > 500 and len(user_platforms[user]) >= 2:
#             influencers.append(user)
            
#     return {
#         "likes": dict(total_likes),
#         "comments": dict(total_comments),
#         "types": type_counter,
#         "platforms": platform_counter,
#         "user_platforms": dict(user_platforms),
#         "influencers": sorted(influencers)
#     }
    

'''
✅ Objetivos:
Calcular:

Total gastado por usuario (defaultdict(int))

Número total de productos distintos por usuario (defaultdict(set))

Cuántas veces se vendió cada producto en total (Counter)

Tiendas únicas donde ha comprado cada usuario (defaultdict(set))

Detectar:

power_users: usuarios que han gastado más de $1000, han comprado al menos 4 productos distintos en más de 1 tienda
'''

# from collections import Counter, defaultdict

# def shopping_activity_analysis(purchases):
#     if not purchases:
#         return {}
    
#     total_spent = defaultdict(int)
#     user_products = defaultdict(set)
#     times_bought = Counter()
#     user_stores = defaultdict(set)
#     power_users = []

#     for purchase in purchases:
#         user, product, category, store, price = purchase
        
#         total_spent[user] += price
#         user_products[user].add(product)
#         user_stores[user].add(store)
        
#         times_bought[product] += 1
        
#     for user in total_spent:
#         if total_spent[user] > 1000 and len(user_products[user]) >= 4 and len(user_stores[user]) > 1:
#             power_users.append(user)
            
#     return {
#         "total_spent": dict(total_spent),
#         "user_products": dict(user_products),
#         "user_stores": user_stores,
#         "power_users": power_users
#     }
    
# purchases = [
#     ("Ana", "Camisa", "Ropa", "Liverpool", 300),
#     ("Ana", "Pantalón", "Ropa", "Zara", 400),
#     ("Ana", "Zapatos", "Calzado", "Zara", 350),
#     ("Ana", "Bolsa", "Accesorios", "Liverpool", 300),
#     ("Luis", "Reloj", "Accesorios", "Sears", 500),
#     ("Luis", "Perfume", "Belleza", "Sears", 700),
#     ("Sofi", "Sudadera", "Ropa", "Zara", 200),
#     ("Sofi", "Camisa", "Ropa", "Zara", 250),
#     ("Sofi", "Zapatos", "Calzado", "Zara", 300),
# ]

# print(shopping_activity_analysis(purchases))
        

'''
🎯 Objetivos:
Calcular:

Tiempo total que cada usuario ha pasado en la biblioteca (defaultdict(int))

Categorías distintas de libros que ha leído cada usuario (defaultdict(set))

Sucursales únicas visitadas por cada usuario (defaultdict(set))

Conteo total de libros leídos por categoría (Counter)

Identificar:

avid_readers: usuarios que han pasado más de 200 minutos, leído libros de al menos 3 categorías distintas, y visitado 2 o más sucursales.
'''

# from collections import Counter, defaultdict

# def library_usage_analysis(records):
#     if not records:
#         return {}
    
#     total_time_spent = defaultdict(int)
#     book_categories = defaultdict(set)
#     user_stores = defaultdict(set)
#     book_counter = Counter()
#     avid_readers = []
    
#     for record in records:
#         user, book_title, category, library_branch, time_spent = record
        
#         total_time_spent[user] += time_spent
#         book_categories[user].add(category)
#         user_stores[user].add(library_branch)
        
#         book_counter[category] += 1
        
#     for user in total_time_spent:
#         if total_time_spent[user] > 200 and len(book_categories[user]) >= 3 and len(user_stores[user]) >= 2:
#             avid_readers.append(user)
            
#     return {
#         'time_spent' : total_time_spent,
#         'book_categories' : book_categories,
#         'user_stores' : user_stores,
#         'avid_readers' : avid_readers
#     }
   
# records = [
#     ("Ana", "1984", "Ficción", "Centro", 60),
#     ("Ana", "El Principito", "Ficción", "Centro", 40),
#     ("Ana", "Sapiens", "Historia", "Norte", 70),
#     ("Ana", "Meditaciones", "Filosofía", "Norte", 60),
#     ("Luis", "Sapiens", "Historia", "Centro", 90),
#     ("Luis", "Meditaciones", "Filosofía", "Centro", 80),
#     ("Sofi", "Cocina Italiana", "Gastronomía", "Sur", 100),
#     ("Sofi", "El arte de amar", "Filosofía", "Sur", 120),
# ]

# print(library_usage_analysis(records))


'''
🎯 Objetivos:
Calcular:

Horas totales leídas por usuario (defaultdict(int))

Géneros explorados por usuario (defaultdict(set))

Ubicaciones de lectura por usuario (defaultdict(set))

Conteo de libros por género (Counter)

Detectar a los "círculo interno" (inner_circle):

Usuarios con más de 180 horas

Que hayan leído en al menos 2 ubicaciones distintas

Y leído libros de 3 o más géneros

Que no tengan ningún status == "incomplete"
'''
# from collections import Counter, defaultdict

# def mystery_club_analysis(memberships):
#     if not memberships:
#         return {}
    
#     total_hours = defaultdict(int)
#     user_genres = defaultdict(set)
#     reading_locations = defaultdict(set)
#     books_by_genre = Counter()
#     incomplete_books = set()
#     inner_circle = []
    
#     for membership in memberships:
#         user, book_title, genre, hour, location, status = membership
        
#         if status == "incomplete":
#             incomplete_books.add(user)
#             continue
        
#         total_hours[user] += hour
#         user_genres[user].add(genre)
#         reading_locations[user].add(location)
#         books_by_genre[genre] += 1
        
#     for user in total_hours:
#         if total_hours[user] > 180 and len(reading_locations[user]) >= 2 and len(user_genres[user]) >= 3 and user not in incomplete_books:
#             inner_circle.append(user)
            
#     return {
#         'total_hours': dict(total_hours),
#         'reading_locations': dict(reading_locations),
#         'user_genres': dict(user_genres),
#         'books_by_genre': dict(books_by_genre),
#         'incomplete_books': incomplete_books,
#         'inner_circle': sorted(inner_circle)
#     }
    
# records = [
#     ("Ana", "El símbolo perdido", "Misterio", 60, "Biblioteca", "complete"),
#     ("Ana", "Inferno", "Thriller", 70, "Casa", "complete"),
#     ("Ana", "Los pilares de la tierra", "Histórico", 60, "Casa", "complete"),
#     ("Luis", "El código Da Vinci", "Misterio", 90, "Biblioteca", "incomplete"),
#     ("Luis", "Ángeles y Demonios", "Misterio", 70, "Biblioteca", "complete"),
#     ("Sofi", "Orgullo y prejuicio", "Romance", 100, "Café", "complete"),
#     ("Sofi", "La Odisea", "Clásico", 90, "Café", "complete"),
#     ("Sofi", "El alquimista", "Filosofía", 80, "Parque", "complete"),
# ]

# print(mystery_club_analysis(records))