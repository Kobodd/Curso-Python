# name= input('Porfabor introduce tu nombre:')
# age= int(input('Introduce tu edad, {0}:'.format(name)))
# print(age)
#
# if age>= 18:
#         print('Eres mayor de edad')
# else:
#         print('No eres mayor de edad, seras mayor de edad en:{0} anyos'.format(18-age))\


# Este codigo tiene un error al definir la funcion donde toca, Se corrigue en el siguiente codigo:
# import random
#
# print('Vamos a jugar a adivinar un numero del 1 al 10')
#
# def bucle():
#
#     adivinar = int(input('Introduce el numero a adivinar:'))
#     numero= random.randint(1,10)
#     if adivinar==numero:
#         print('Has acertado el numero.')
#     else:
#         print('Vuelve a intentarlo')
#         bucle()


import random
def bucle():
    if adivinar > 10:
    adivinar = int(input('Introduce el numero a adivinar:'))
    numero= random.randint(1,10)
    if adivinar==numero:
        print('Has acertado el numero.')
    else:
        print('Vuelve a intentarlo')
        bucle()

print('Vamos a jugar a adivinar un numero del 1 al 10')
bucle()

 # mismo programa a los dos anteriores pero sin funciones con bucle While
# import random
# print('Vamos a jugar a adivinar un numero del 1 al 10')
#
# numero=random.randint(1,10)
# adivinar = int(input('Introduce el numero a adivinar:'))
#
# print(numero)
#
# while numero!=adivinar:
#     print('vuelve a intentarlo')
#     adivinar = int(input('Introduce el numero a adivinar:'))
#
# print('Muy bien has acertado')