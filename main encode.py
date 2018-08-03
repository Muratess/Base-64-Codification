import os
# importa o alfabeto
import string
# função de quebra de palavras
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
# lista completa com todos os caracteres da base 64
alphabet_base_64 = ascii_uppercase + ascii_lowercase + numbers + specials

# começa a codificação
def encode_base64(word):
    binaries = []
    word_binary_len = 0
    cod_word = []

    # percorrendo a palavra
    for w in word:
        # encontra a localização do char na tabela ascii
        word_number_ascii = ord(w)
        # transformando em binarios a localização do char, e completando com zeros a esquerda se preciso
        word_binarie = format(word_number_ascii, '08b')
        # add na lista de binarios
        binaries.append(word_binarie)

    # verifica o tamanho do binario para ver se esta do tamanho certo
    for b in binaries:
        word_binary_len += len(b)
    # se não estiver no tamanho ele completa com zeros a esquerda, e depois junta tudo em uma string
    if word_binary_len < 24:
        binaries = ''.join(binaries)
        binaries = '{:024d}'.format(int(binaries))
    # se estiver do tamanho certo ele só junta tudo em uma string  
    else:
        binaries = ''.join(binaries)

    # separa em grupos de 6 bits
    binaries = wrap(binaries, 6)
    # transforma os binarios em decimais novamente,
    # e depois pelo decimal encontra o indice na lista da base e coloca o valor correspodente
    for b in binaries:
        decimal = int(b, 2)
        cod_word.append(alphabet_base_64[decimal])

    return ''.join(cod_word)
# esta terminada a decodificação, agora falta decodificar

    binaries = []
    decoded_word = []
    # percorre o texto codificado char por char pegando seu indice na lista da base, depois transforma em binario
    # completando com zeros a esquerda e depois cria uma lista com os binarios para a decodificação
    for h in hash_text:
        decimal = alphabet_base_64.index(h)
        binarie = '{:06b}'.format(decimal)
        binaries.append(binarie)

    binaries = ''.join(binaries)
    binaries = wrap(binaries, 8)
    # tranforma os binario em decimais novamente, e depois encontra pelo
    # indice na lista da base o char correspondente
    for b in binaries:
        integer_word = int(b, 2)
        decoded_word.append(chr(integer_word))

    return ''.join(decoded_word)

# aqui ele le o arquivo depois da codificação escreve no arquivo
def main():
    filename = 'test.txt'
    with open(filename, 'r') as file:
        text_encoded = encode_base64(file.read())

    os.remove(filename)

    with open(filename, 'w') as file:
        file.write(text_encoded)


if __name__ == '__main__':
    main()