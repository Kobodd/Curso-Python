# # Name: Pedro Garcia Cano
# # Section:
# # Date: 15/12/2016 21:20
# # hw1.py
#
# ##### Template for Homework 1, exercises 1.2-1.5 ######
#
# print ("********** Exercise 1.1 **********\n")
#
# print('Hello, World!!!\n')
#
# print ("********** Exercise 1.2 **********\n")
#
# barras = '  |  |  \n'
# lineas = '--------\n'
# print('  |  |  ')
# print('--------')
# print('  |  |  ')
# print('--------')
# print('  |  |  ')
#
# print('{}{}{}{}{}'.format(barras,lineas,barras,lineas,barras))
# # Do your work for Exercise 1.2 here
#
# print ("********** Exercise 1.3 **********\n")
#
# # Do your work for Excercise 1.3 here. Hint - how many different
# #
#
# a = 'Hello, World!!'
# b = 'and goodbye...'
#
# print (a + b + '\n')
#
# print ("********** Exercise 1.4 **********\n")
#
# x = 5 + 7
#
# print (x)
#
# y = x +10
#
# print (y)
#
# print ("*********  Part I *************\n")
#
# x = 5 **2.0
#
# print(x)
#
# print ("********* Part II *************\n")
# import math
# x =(3*5)/(2+3)
# y = math.sqrt(7 + 9) * 2
# z = (4 -7) ** 3
# w = math.sqrt(-19 + 100)
# m = (6%4)
# print(x, y, z, w, m)
#
# print ("********* Part III ************\n")
#
#
# x = (7+3)+5 *3
# y = 7+(3+5) *3
#
# print(x)
# print(y)
#
# print ("********** Exercise 1.5 **********\n")
#
# name = input('Introduce tu nombre:')
# apellido = input('Introduce tu apellido')
# print('Fecha de nacimiento:')
# mes = input('Mes?')
# dia = input('Dia?')
# año = input('Año?')
#
# print('{} {} nacio el {} {} {}'.format(name,apellido,dia,mes,año))

# print ("********** Exercise 1.7 **********\n")
#
# p1 = input('Please Enter Your Choise.')
# p2 = input('Please Enter Your Choise.')
#
# if (p1 == 'Rock' or p1 == 'Scissors' or p1 == 'Paper' or p2 == 'Rock' or p2 == 'Scissors' or p2 == 'Paper'):
#     if (p1 == 'Rock'):
#         if p2 == 'Rock':
#             print('Tie')
#         elif p2 == 'Scissors':
#             print('Player 1 wins')
#         else:
#             print('Player 2 wins')
#
#     if (p1 == 'Scissors'):
#         if p2 == 'Scissors':
#             print('Tie')
#         elif p2 == 'Paper':
#             print('Player 1 wins')
#         else:
#             print('Player 2 wins')
#
#     if (p1 == 'Paper'):
#         if p2 == 'Paper':
#             print('Tie')
#         elif p2 == 'Rock':
#             print('Player 1 wins')
#         else:
#             print('Player 2 wins')
#
# else:
#     print('This is not a valid object selectionm.')

# print ("********** Exercise 1.7 **********\n")
#
# print ("********** Exercise 1.7.1 **********\n")
#
# for i in range(2,10):
#     print(1/i)
#
# print ("********** Exercise 1.7.2 **********\n")
#
# numero = input('Introduce un numero:')
# numero = int(numero)
#
# while (numero > 0):
#     print(numero)
#     numero -=1
#
# print ("********** Exercise 1.7.3 **********\n")
#
# number= input('Por Fabor Introduce el numero:')
# exponencial= input('Introduce a cuanto lo quieres elevar')
#
# for i in range((int(number)),(int(number)+1)):
#     print('{}'.format(i**int(exponencial)))

print ("********** Exercise 1.7.4 **********\n")

numero = input('Introduce un numero:')

numero = int(numero)

while (numero %2 != 0):
    numero = int(input('Introduce un numero:'))

print('Felicidades has introducido un multiplo de 2')