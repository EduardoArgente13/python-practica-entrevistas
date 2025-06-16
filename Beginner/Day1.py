#Band Name Generator

# print("Welcome to the Band Generator") 
# city = input("What's the name of the city you grew up?: ")
# pet = input("Now, write the name of you first pet: ")
# print("Great! the name of yourt band is: ")
# print (city + " " + pet)

#Declarar una variable con cad tipo y mostralo con print

# name = "Lalo"
# age = 26
# gpa = 3.93
# active = True

# print(type(name)) #str
# print(type(age)) #int
# print(type(gpa)) #float
# print(type(active)) #bool

# Aritméticos
# a + b, a - b, a * b, a / b, a % b, a ** b

# Comparación
# a == b, a != b, a > b, a < b, a >= b, a <= b

# Lógicos
# and, or, not

#Comparar 2 valores
# def compare(input1, input2):
#     if input1 > input2:
#         print(f"{input1} is bigger than {input2}")
#     elif input2 > input1:
#         print(f"{input2} is bigger than {input1}")
#     else:
#         print(f"{input1} and {input2} are the same")
    
# num1 = input("Write the first number")
# num2 = input("Write the second number")

# compare(num1, num2)


#Range de edad

# def ageRange(age):
#     if age < 18:
#         print ("Menor de edad")
#     elif age <= 30:
#         print ("Joven Adulto")
#     else: 
#         print("Adulto")
        
# age = int(input("How old are you? "))
# ageRange(age)

#Declarar una listc on 5 numeros, y usar un bucle for para calcular la suma total

# nums = [1, 2, 3, 4, 5]

# def listSum(nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total

# print(listSum(nums))



#Funcion que recibe 2 numeros y regresa su producto

# def product(num1, num2):
#     prod = num1 * num2
#     return (f"The product of {num1} and {num2} is {prod}")

# num1 =int(input("Write the first number: "))
# num2 = int(input("Write the second number: "))

# print(product(num1, num2))


#Funcion es Par o Impar

# def par_o_impar(n):
#     if n % 2 == 0:
#         return "Es Par"
#     else:
#         return "Es impar"

# for num in range(1, 21):
#     res = par_o_impar(num)
#     print(f"El numero {num} es {res}")

def merge(nums1, m, nums2, n):
    i = m - 1 # Puntero que apunta al ultimo numero "real" de nums1
    j = n - 1 #Puntero que apunta al ultimo numero de nums2
    k = m + n - 1 #Punteroq ue apunta al ultimo espacion de nums1
    
    #Mientras aun tengamos numeros en nums2 y nums1 para comparar
    while i >= 0 and  j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[j] #Mueve el numero mas grande al final
            i -= 1
        else:
            nums1[k] = nums2[j] #Mueve el numero mas grande al final
            j -= 1
        
        k -= 1
        
        #si todavioa quedan numero en nums2 (nums1 ya se uso todo)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        

nums1 = [4, 5, 6, 0, 0, 0]
m = 3
nums2 = [1, 2, 3]
n = 3

merge(nums1, m, nums2, n)

print(nums1) 