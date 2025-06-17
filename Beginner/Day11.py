'''Crear un diccionario promedios donde cada estudiante sea la clave y el valor sea su promedio de calificaciones.

Crear un diccionario materias donde cada estudiante tenga el set de materias que cursó.

Obtener una lista destacados con los estudiantes que tienen promedio mayor a 8.5 y cursaron más de 2 materias.
'''

# def grades_record(grades):
#     if not grades:
#         return {}
    
#     averages = {}
#     total_scores = {}
#     subjects = {}
#     subject_counts = {}
#     outstandings = []
    
#     for student, subject, score in grades: 
#         total_scores[student] = total_scores.get(student, 0) + score
#         subject_counts[student] = subject_counts.get(student, 0) + 1
        
#         subjects.setdefault(student, set()).add(subject)
    
#     for student in total_scores:
#         averages[student] = total_scores[student] / subject_counts[student]
#         if averages[student] > 8.5 and subject_counts[student] > 2:
#             outstandings.append(student)
    
    
#     return {'averages' : averages, 'subjects' : subjects, 'outstandings' : sorted(outstandings)}
    



'''Calcular el promedio de calificaciones por usuario.

Guardar las categorías distintas en las que cada usuario ha dejado reseña.

Identificar a los usuarios que:

Tienen más de 2 reseñas.

Tienen un promedio mayor a 4.0.

Han opinado en más de 1 categoría.
'''

# def product_review_analysis(reviews):
#     if not reviews:
#         return {}
    
#     avg_rating = {}
#     top_rating = {}
#     user_products = {}
#     categories = {}
#     fans = []
    
#     for review in reviews:
#         user, product, category, rating = review
        
#         top_rating[user] = top_rating.get(user, 0) + rating
#         user_products[user] = user_products.get(user, 0) + 1
        
#         categories.setdefault(user, set()).add(category)
        
#     for user in top_rating:
#         avg_rating[user] = top_rating[user] / user_products[user]
#         if avg_rating[user] > 4.0 and user_products[user] > 2 and len(categories[user]) > 1:
#             fans.append(user)
            
#     return {
#         'average' : avg_rating,
#         'categories' : categories,
#         'fans' : fans
#     }
    
# reviews = [
#     ("Ana", "Laptop", "Electrónica", 5),
#     ("Luis", "Cámara", "Electrónica", 4),
#     ("Ana", "Libro", "Libros", 4),
#     ("Sofi", "Cafetera", "Hogar", 3),
#     ("Ana", "Auriculares", "Electrónica", 5),
#     ("Luis", "Libro", "Libros", 5),
#     ("Luis", "Toalla", "Hogar", 2),
# ]

# print(product_review_analysis(reviews))



'''
Tu objetivo es construir una función restaurant_order_analysis(pedidos) que:

🎯 Objetivos:
Calcule cuánto gastó cada cliente en total (total_spent).

Cuente cuántos platillos distintos pidió cada cliente (distinct_dishes).

Identifique a los clientes premium: aquellos que gastaron más de $1000 y usaron al menos 2 métodos de pago distintos.
'''

# def restaurant_order_analysis(orders):
#     if not orders:
#         return {}
    
#     total_spent = {}
#     distinct_dishes = {}
#     payment_methods = {}
#     premium_clients = []
    
#     for order in orders:
#         order_id, client, dish, price, payment_method = order
        
#         total_spent[client] = total_spent.get(client, 0) + price
#         distinct_dishes.setdefault(client, set()).add(dish)
#         payment_methods.setdefault(client, set()).add(payment_method)
        
#     for client in total_spent:
#         if total_spent[client] > 1000 and len(payment_methods[client]) >= 2:
#             premium_clients.append(client)
            
#     return {
#         'total_spent' : total_spent,
#         'distinct_dishes' : distinct_dishes,
#         'premium_clients' : premium_clients
#     }
    
# orders = [
#     (1, "Ana", "Tacos", 150, "efectivo"),
#     (2, "Luis", "Pizza", 300, "tarjeta"),
#     (3, "Ana", "Ensalada", 120, "tarjeta"),
#     (4, "Luis", "Tacos", 300, "tarjeta"),
#     (5, "Sofi", "Hamburguesa", 200, "efectivo"),
#     (6, "Ana", "Pizza", 200, "efectivo"),
#     (7, "Luis", "Ensalada", 350, "efectivo"),
#     (8, "Luis", "Sopa", 200, "transferencia"),
#     (9, "Sofi", "Sopa", 400, "efectivo"),
# ]

# print(restaurant_order_analysis(orders))



'''
Tienes una lista de reservas en hoteles con el siguiente formato:

python
Copiar código
(bookings) = [
    (cliente, hotel, ciudad, noches, precio_noche, estado)
]
🎯 Objetivos:
Calcular el gasto total por cliente (solo reservas confirmadas).

Guardar los hoteles diferentes en los que cada cliente se ha alojado.

Guardar las ciudades distintas que ha visitado.

Identificar a los clientes frecuentes:

Han gastado más de 2000.

Se hospedaron en al menos 3 hoteles distintos.

Visitaron al menos 2 ciudades distintas.

Y no tienen reservas canceladas.
'''

def hotel_booking_analysis(bookings):
    if not bookings:
        return {}
    
    total_spent = {}
    visited_hotels = {}
    visited_cities = {}
    cancelled = set()
    premium_clients = []
    
    for booking in bookings:
        client, hotel, city, nights, price, status = booking
        
        if status == 'cancelled':
            cancelled.add(client)
            continue
        
        total_spent[client] = total_spent.get(client, 0) + (price * nights)
        
        visited_hotels.setdefault(client, set()).add(hotel)
        visited_cities.setdefault(client, set()).add(city)
        
    for client in total_spent:
        if total_spent[client] > 2000 and len(visited_hotels[client]) >= 3 and len(visited_cities[client]) >= 2 and client not in cancelled:
            premium_clients.append(client)
            
    return {
        "total_spent": total_spent,
        "visited_hotels": visited_hotels,
        "visited_cities": visited_cities,
        "premium_clients": premium_clients
    }

bookings = [
    ("Ana", "Hotel Azul", "CDMX", 3, 500, "confirmed"),    # 1500
    ("Ana", "Hotel Verde", "Guadalajara", 2, 400, "confirmed"),  # 800 → Total: 2300 ✅
    ("Ana", "Hotel Rojo", "CDMX", 1, 200, "confirmed"),     # +200 → Hoteles: 3, Ciudades: 2 ✅
    
    ("Luis", "Hotel Azul", "CDMX", 2, 500, "cancelled"),    # ❌ Cancelado
    ("Luis", "Hotel Rojo", "Monterrey", 2, 600, "confirmed"), # 1200, pero solo 1 hotel confirmado ❌
    
    ("Sofi", "Hotel Sol", "CDMX", 2, 300, "confirmed"),     # 600
    ("Sofi", "Hotel Luna", "CDMX", 1, 200, "confirmed"),    # 200
    ("Sofi", "Hotel Estrella", "CDMX", 3, 200, "confirmed"), # 600 → Total: 1400, 3 hoteles, pero 1 ciudad ❌

    ("Marco", "Hotel Alfa", "Puebla", 2, 700, "confirmed"), # 1400
    ("Marco", "Hotel Beta", "Querétaro", 2, 500, "confirmed"), # 1000 → Total: 2400
    ("Marco", "Hotel Gama", "CDMX", 1, 300, "confirmed"),   # +300 → 3 hoteles, 3 ciudades ✅
]

print(hotel_booking_analysis(bookings))

