# # Name: Pedro Garcia Cano
# # Section:
# # Date: 15/12/2016 21:20

frase = input('Please Enter a Phrase:')
frasecod = []
shift = input('Introduce la codificacion que quieres:')

# converts a letter to ascii code

ascii_code = [ord(c) for c in frase]

shift = int(shift)
for o in ascii_code:
    ascii_code = o + shift
    frasecod.append(ascii_code)

# converts ascii code to a letter

letter_res = "".join([chr(c) for c in frasecod])


print (letter_res)