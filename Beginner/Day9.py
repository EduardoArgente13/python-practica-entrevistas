def complete_sales_analysis(sales):
    if not sales:
        return {}
    
    client_total = {}
    client_products = {}
    client_cities = {}
    
    for sale in sales:
        client = sale[0]
        product = sale[1]
        city = sale[2]
        amount = sale[3]
        
        client_total[client] = client_total.get(client, 0) + amount
        
        if client not in client_products:
            client_products[client] = set()
        client_products[client].add(product)
        
        if client not in client_cities:
            client_cities[client] = set()
        client_cities[client].add(city)
        
    res = {}
    for client in client_total:
        res[client] = {
            'total_gastado' : client_total[client],
            'productos' : client_products[client],
            'ciudades' : client_cities[client]
        }
        
    return res

sales = [
    ("Ana", "Laptop", "CDMX", 15000),
    ("Luis", "Tablet", "Guadalajara", 6000),
    ("Ana", "Mouse", "CDMX", 500),
    ("Carlos", "Laptop", "Monterrey", 14500),
    ("Luis", "Laptop", "Guadalajara", 14800),
    ("Ana", "Tablet", "Guadalajara", 6200),
    ("Carlos", "Mouse", "CDMX", 700),
    ("Ana", "Laptop", "CDMX", 15200)
]

analysis = complete_sales_analysis(sales)

# Dados lo datos  escribir una funcion que reciba el diccionario generado por complete sales analysis y devuelva una lista filtrada con los nombre de las personas que han gastado mas de 20000 y han comprado en mas de una ciudad solamente

# def filter_top_clients(analysis):
#     if not analysis:
#         return []
    
#     res = []
    
#     for client, data in analysis.items():
#         spent = data['total_gastado']
#         num_cities = len(data['ciudades'])
        
#         if spent > 20000 and num_cities > 1:
#             res.append(client)
            
#     return sorted(res)

# print(filter_top_clients(analysis))



# Dado los datos de la funcion complete_sales_analysis devolcer una lista de clientes que hayan comprado mas de 2 productos y hddayan hecho mas de una compra

# def multipurchase_clients(analysis):
#     if not analysis:
#         return []
    
#     res = []
    
#     for client, data in analysis.items():
#         purchases = len(data['productos'])
#         cities = len(data['ciudades'])
        
#         if purchases > 2 and cities > 1:
#             res.append(client)
            
#     return sorted(res)

# print(multipurchase_clients(analysis))



#Dada una lista de envios en formato tupla: Calcular cuántas unidades totales recibió cada cliente, Guardar los productos diferentes que cada cliente recibió
# Guardar las ciudades diferentes a donde se le han enviado pedidos, Devolver una lista de clientes que: Hayan recibido más de 30 unidades, Hayan recibido envíos en más de una ciudad, No tengan pedidos pendientes

def shipment_analysis(shipments):
    if not shipments:
        return {}
    
    total_units = {}
    products = {}
    cities = {}
    remainings = set()
    
    for ship in shipments:
        client, product, city, quantity, delivery_state = ship
        
        total_units[client] = total_units.get(client, 0) + quantity
        
        if client not in products:
            products[client] = set()
        products[client].add(product)
        
        if client not in cities:
            cities[client] = set()
        cities[client].add(city)
        
        if delivery_state == 'remaining':
            remainings.add(client)
    
    res = []
    for client in total_units:
        if total_units[client] > 30 and len(cities[client]) > 1 and client not in remainings:
            res.append(client)
            
    return sorted(res)


shipments = [
    ("Ana", "Laptop", "CDMX", 10, "delivered"),
    ("Ana", "Tablet", "CDMX", 5, "delivered"),
    ("Ana", "Mouse", "Guadalajara", 20, "delivered"),
    ("Luis", "Tablet", "Guadalajara", 15, "remaining"),
    ("Luis", "Tablet", "Guadalajara", 10, "delivered"),
    ("Carlos", "Mouse", "Monterrey", 12, "delivered"),
    ("Carlos", "Mouse", "CDMX", 12, "delivered"),
    ("Carlos", "Mouse", "CDMX", 8, "delivered"),
]

print(shipment_analysis(shipments))


def complete_analysis(shipments):
    if not shipments:
        return {}
    
    total_units = {}
    cities = {}
    products = {}
    remainings = set()
    
    
#