palabra= ["casa","oro", "Oso","eres","somo","somos","escalera","RoTor"]

# for i in palabra:
#     print("{}".format(i))

# for i in palabra:
#     print(palabra[-i])


for i in palabra:

    palabragirada = ''
    i = i.lower()

    for char in i:

        palabragirada = char + palabragirada

    if palabragirada==i:
        print(i)
    else:
        print('No es igual')

# palabra = palabra[::-1]
#
# print(palabra)