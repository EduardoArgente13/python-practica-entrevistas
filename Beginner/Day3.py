#Escribe un programa que pida un número y diga si es positivo, negativo o cero.
def qualification(number):
    if not number:
        return None
    
    if number == 0:
        type = "Zero"
    elif number > 0:
        type = "Positive"
    else:
        type = "Negative"
        
    return type
        
        

#Crea una lista de 5 nombres y recórrela con un for imprimiendo: "Hola, <nombre>".

def name_list(names):
    if not names:
        return []
    
    for name in names:
        print(f"Hola, {name}")
        

#Haz un programa que cuente del 1 al 10 con un while.


x = 1
    
while x < 11:
    print(x)
    x += 1
        

#Extra: crea una lista vacía y usa un for para llenarla con los números del 1 al 5.

empty = []

for i in range(1, 6):
    empty.append(i)

print(empty)

    