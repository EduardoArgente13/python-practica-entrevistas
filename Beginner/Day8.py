# Dada una lista Sales Total gastado por cada cliente, Productos comprados por cada cliente (sin repetir), Ciudades donde cada cliente ha comprado, Clientes que compraron más de 2 productos diferentes, Gasto total por ciudad

# def sales_analysis(sales):
#     if not sales :
#         return {}
    
#     client_total = {}
#     client_products = {}
#     client_cities = {}
    
#     for sale in sales:
#         client = sale[0]
#         amount = sale[3]
#         product = sale[1]
#         city = sale[2]
        
#         # Total Gastado
#         client_total[client] = client_total.get(client, 0) + amount
        
#         # Productos Comprados
#         if client not in client_products:
#             client_products[client] = set()
#         client_products[client].add(product)
        
#         # Ciudades de Compra
#         if client not in client_cities:
#             client_cities[client] = set()
#         client_cities[client].add(city)
        
#     return client_total, client_products, client_cities
    
# sales = [
#     ("Ana", "Laptop", "CDMX", 15000),
#     ("Luis", "Tablet", "Guadalajara", 6000),
#     ("Ana", "Mouse", "CDMX", 500),
#     ("Carlos", "Laptop", "Monterrey", 14500),
#     ("Luis", "Laptop", "Guadalajara", 14800),
#     ("Ana", "Tablet", "CDMX", 6200),
#     ("Carlos", "Mouse", "Monterrey", 700),
#     ("Ana", "Laptop", "CDMX", 15200)
# ]

# print(sales_analysis(sales))



# Dado un listado de ventas, escribe una funcion que devuelva un diccionario con la estructura definida

# def complete_sales_analysis(sales):
#     if not sales:
#         return {}
    
#     client_total = {}
#     client_products = {}
#     client_cities = {}
    
#     for sale in sales:
#         client = sale[0]
#         product = sale[1]
#         city = sale[2]
#         amount = sale[3]
        
#         client_total[client] = client_total.get(client, 0) + amount
        
#         if client not in client_products:
#             client_products[client] = set()
#         client_products[client].add(product)
        
#         if client not in client_cities:
#             client_cities[client] = set()
#         client_cities[client].add(city)
        
#     res = {}
#     for client in client_total:
#         res[client] = {
#             'total_gastado' : client_total[client],
#             'productos' : client_products[client],
#             'ciudades' : client_cities[client]
#         }
        
#     return res
    
# sales = [
#     ("Ana", "Laptop", "CDMX", 15000),
#     ("Luis", "Tablet", "Guadalajara", 6000),
#     ("Ana", "Mouse", "CDMX", 500),
#     ("Carlos", "Laptop", "Monterrey", 14500),
#     ("Luis", "Laptop", "Guadalajara", 14800),
#     ("Ana", "Tablet", "Guadalajara", 6200),
#     ("Carlos", "Mouse", "CDMX", 700),
#     ("Ana", "Laptop", "CDMX", 15200)
# ]

# resultado = complete_sales_analysis(sales)
# from pprint import pprint
# pprint(resultado)

    
    