# Como dito por um importante personagem de um igualmente memorável filme: 
# "palavras são, na minha nada humilde opinião, nossa inesgotável fonte de magia
#  [...]". Evidentemente, seria difícil formar palavras se não houve uma alfabeto 
# bem estabelecido e divulgado, assim como em nosso alfabeto latino.

# O alfabeto latino é composto por letras, começando em 'A' e encerrando em 'Z'. 
# São vinte e seis caracteres diferentes, se desconsiderarmos as acentuações e as 
# diferenças entre letras maiúsculas e minúsculas.

# Harry, um garoto muito estudioso, percebeu que é possível inclusive desenhar
# usando letras. Em um dos desenhos, Harry escreve na primeira linha de uma folha 
# o primeiro caractere do alfabeto, na segunda linha escreve duas vezes o segundo 
# caractere, na terceira linha escreve três vezes o terceiro caractere e assim por 
# diante. Harry percebeu que com isso consegue formar um triângulo alfabético,
# semelhante ao visto na Figura 1.

# Como Harry precisa estudar para realizar uma prova de programação (que para ele 
# também é uma forma de magia!), pediu para você ajudá-lo a automatizar os desenhos 
# de "triângulos alfabéticos", criando um programa que receba como entrada um número 
# inteiro N (1 <= N <= 26) e que desenhe um triângulo com exatas N linhas, seguindo a
#  mesma estratégia descrita no texto.

# Entrada

# Um número inteiro N (1 <= N <= 26).

# Saída

# Um triângulo alfabético com exatas N linhas e com a mesma estratégia de construção
#  mencionada no texto. Note que as letras são sempre maiúsculas.


alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numero = int(input())
contador_linha = 0
contador_letra = 0

if numero > 0 and numero <= 26:
    while contador_linha <= numero:
        contador_letra = 0
        while contador_letra < contador_linha:
            print(alfabeto[contador_linha-1], end='')
            contador_letra+=1
        print('')
        contador_linha+=1

