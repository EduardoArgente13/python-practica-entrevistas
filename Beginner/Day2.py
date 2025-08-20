#Day 2

a = 15
b = 4

suma = a + b
resta = a - b
mult = a * b
div = a / b
power = 7 ** 3

print(f"Suma = {suma}")
print(f"Resta = {resta}")
print(f"Multiplicación = {mult}")
print(f"División = {div}")
print(f"Potencia = {power}")

if 15 % 2 == 0:
    print("par")
else:
    print("impar")


# Conversión de edad
age_string = "26"
age = int(age_string)
print(f"Tengo {age*12} meses o {age*12*30} días de edad")


# Calculadora
def calculator(input1, input2):
    return {
        "addition": input1 + input2,
        "substraction": input1 - input2,
        "multiplication": input1 * input2,
        "division": input1 / input2,
    }


# Par/Impar y Positivo/Negativo/Cero
def odd_even(value):
    if value % 2 == 0:
        type1 = "Even"
    else:
        type1 = "Odd"

    if value == 0:
        type2 = "Zero"
    elif value > 0:
        type2 = "Positive"
    else:
        type2 = "Negative"

    print(f"The number {value} is {type1} and {type2}")
