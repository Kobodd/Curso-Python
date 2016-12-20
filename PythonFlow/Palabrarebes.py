# for i in palabra:
#     print("{}".format(i))

# for i in palabra:
#     print(palabra[-i])


palabra= ["casa","oro", "Oso","eres","somo","somos","escalera","RoTor"]

palabramin = ''
lista= []

for i in palabra:

    palabragirada = ''

    palabramin = i.lower()

    for char in palabramin:
        palabra = palabra[::-1]
        # palabragirada = char + palabragirada

    if palabragirada==palabramin:
        lista.append(i)

print(lista)


