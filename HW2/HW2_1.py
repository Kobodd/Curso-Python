import math

# # Ejercicio 2.0
# def f1(x):
#     print(x + 1)
# def f2(x):
#     return(x + 1)
#
# f1(3)
# f2(3)
# print(f1(3))
# print(f2(3))
# print(f2(3) + 1)

# Ejercicio 2.2
#
# class divisible:
#     def is_divisible(m,n):
#         if ((m % n) == 0):
#             return ('true')
#         else:
#             return('False')
# class equals:
#     def not_equals(m,n):
#         if ((m - n) == 0):
#             return ('true')
#         else:
#             return('False')
#
# resultado = divisible.is_divisible(2,2)
# iguales = equals.not_equals(0,3)
# print(resultado)
# print(iguales)

# # Ejercicio 2.3
#
# radians = (90.0 / 360.0) * 2 * math.pi
# print(math.sin(radians))
#
# ## 1 - multadd function
#
# def multadd(a,b,c):
#     return(a*b+c)
#
# print(multadd(6,3,3))
#
# ## 2 - Equations
#
# angle_test = multadd(1,math.sin(math.pi/4),math.cos(math.pi/4)/2)
# print(angle_test)
#
# ceiling_test = multadd(1,math.ceil(276/19.0),2*math.log(12,7))
# print(ceiling_test)
#
# ## 3 - yikes function
# def yikes(x):
#     return multadd(x,math.exp(-x),math.sqrt((1-math.exp(-x))))
#
# print(yikes(5))


# Ejercicio 2.5
# class quadraticformula:
#     def calculos(a,b,c):
#         primero = 4*a*c
#         segundo = (b*b)-primero
#         if (segundo < 0):
#             return('numero complejo')
#         else:
#             raizcuadrada = math.sqrt(segundo)
#             resultado1 = ((-b) + (raizcuadrada)) / (2*a)
#             resultado2 = ((-b) - (raizcuadrada)) / (2*a)
#
#             return (resultado1,resultado2)
#
# resultadofinal = quadraticformula.calculos(4,2,-3)
# print(resultadofinal)


# Ejercicio 2.7

# def sum_all(number_list):
#
#     total = 0
#     for num in number_list:
#         total += num
#
#     return total
#
# def cumulative_sum(number_list):
#
#     count = 0
#     sum = 0
#     normal = number_list[:]
#
#     for num in number_list:
#         sum += num
#         number_list[count] = sum
#         count += 1
#
#     return number_list, normal
#
# print (cumulative_sum([4, 3, 6]))


# Ejercicio 2.8

# class_taken = input("\nList the classes you took,"
#                         " separated by a comma\n")
# grade_earned = input("List the corresponding grade you"
#                      " earned, separated by a comma\n")

# def report_card(grade_earned):
#
#     total = 0
#     for num in int(grade_earned):
#         total += num
#
#     return total/len(grade_earned)
#
# print("\nAverage GPA:\n", report_card(grade_earned))

# Ejercicio 2.9


# Funcion para mirar si la primera letra es vocal
def find(str, ch):
    index = 0
    while index < len(str):
        if str[index] == ch:
            return index
        index = index + 1
    return -1

VOWELS = ['a', 'e', 'i', 'o', 'u']

def pig_latin(word):
    # Primera letra vocal?
    if (find(VOWELS, word[0]) == True):
        # devolvemos la palabra con Hay al final
        convocal = word[1:] + word[0]
        convocal += "hay"
        return convocal
    elif len(word) > 0:
        # Movemos la primera letra al final y ponemos ay
        sinvocal = word[1:] + word[0]
        sinvocal += "ay"
        return sinvocal
    else:
        return "error dude"

# Prueba 2.9

print("pirates en pig latin:", pig_latin("irates"))