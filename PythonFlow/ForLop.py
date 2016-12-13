# palabra = 'hola','como','estas'
#
# for i in palabra:
#     print(i)

# for i in range(0,10):
#     for i in range(0,10):
#         for i in range(0,2):
#             print(i)

ipAddress = input("Please enter an IP address: ")

segment = 1
segment_length = 0
character = ""

for character in ipAddress:
    if character == '.':
        print("segment {} contains {} characters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

# unless the final character in the string was a . then we haven't printed the last segment
if character != '.':
    print("segment {} contains {} characters".format(segment, segment_length))