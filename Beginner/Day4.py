#Day 4

'''1. format_name
Escribe format_name(nombre, apellido, *, mayus=False) que regrese "Apellido, Nombre".
Si mayus=True, regresa en MAYÚSCULAS.'''

def format_name(name, lastname, upper=False):
    if upper == True:
        lastname = lastname.upper()
        name= name.upper()
    return lastname + ", " +name

print(format_name(name="Lalo", lastname="Argente", upper=True))

'''2. stats
stats(nums) regresa tres valores: (mínimo, máximo, promedio).
Si la lista está vacía → ValueError.'''

def stats(nums):
    if not nums:
        raise ValueError("La lista está vacía")
    
    mx = max(nums)
    mn = min(nums)
    avg = sum(nums) / len(nums)
    
    return (mn, mx, avg)
    
nums = [1, 2, 3, 4, 5]
print(stats(nums))

'''3. safe_div
safe_div(a, b, *, decimals=2) divide a/b y redondea a decimals.
Si b == 0 → regresa None (usa guard clause).'''

def safe_div(a, b, decimals=2):
    if b == 0:
        return None
    
    res = round(a / b, decimals)
    
    return res


'''4. apply_all
apply_all(func, *args, **kwargs) llama a func(*args, **kwargs) y regresa una tupla: (resultado, tipo_del_resultado).'''

def apply_all(func, *args, **kwargs):
    var = func(*args, **kwargs)
    return var, type(var)


'''5. inplace_or_copy
inplace_or_copy(lista, x, *, inplace=True)

Si inplace=True, agrega x modificando la lista original y la regresa.

Si False, trabaja sobre una copia y regresa la nueva lista (la original intacta).'''

def inplace_or_copy(lista, x, inplace=True):
    if inplace == True:
        lista.append(x)
        return lista
    else:
        new_list = lista.copy()
        new_list.append(x)
        return new_list
