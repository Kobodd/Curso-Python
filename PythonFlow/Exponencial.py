print('Exponencial de numero introducido por teclado.')
number= input('Por Fabor Introduce el numero:')
exponencial= input('Introduce a cuanto lo quieres elevar')

for i in range((int(number)),(int(number)+1)):
    print('{}'.format(i**int(exponencial)))

# import pprint
#
# inputFile = input("File Name : ")
# count = {}
#
# with open(inputFile, 'r') as info:
#     readFile = info.read()
#     for character in readFile.upper():
#         count.setdefault(character, 0)
#         count[character] = count[character] + 1
#
# value = pprint.pformat(count)
# print(value)
#
#
# import pprint
#
# inputFile = ('%12.50f' %(22/7))
# count = {}
#
# for character in str(inputFile).upper():
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
#
# value = pprint.pformat(count)
# print(value)