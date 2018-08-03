import os
import string
from textwrap import wrap

# alfabeto com letras maiusculas
ascii_uppercase = list(string.ascii_uppercase)

# alfabeto om letras minusculas
ascii_lowercase = list(string.ascii_lowercase)

# barra e o caractere de adiçao
specials = ['/', '+']

# numeros de 0 a 9
numbers = []
for n in range(10):
    numbers.append(str(n))

alphabet_base_64 = ascii_uppercase + ascii_lowercase + numbers + specials


def decode_base64(hash_text):
    binaries = []
    decoded_word = []
    # ele le char por char e pega o indice na lista depois transforma
    # para binario e add em uma lista com todos os binsrios
    for h in hash_text:
        decimal = alphabet_base_64.index(h)
        binarie = '{:06b}'.format(decimal)
        binaries.append(binarie)
    # junta todos os binarios em uma lista e depois quebra em 8 bits
    binaries = ''.join(binaries)
    binaries = wrap(binaries, 8)
    # tranforma em decimal
    for b in binaries:
        integer_word = int(b, 2)
        decoded_word.append(chr(integer_word))
    # pega o indice e pega o correspondente na lista
    return ''.join(decoded_word)

# ele vai ler o arquivo depois ecever o texto decodoficado
def main():
    filename = 'test.txt'
    with open(filename, 'r') as file:
        text_encoded = decode_base64(file.read())

    os.remove(filename)

    with open(filename, 'w') as file:
        file.write(text_encoded)


if __name__ == '__main__':
    main()
