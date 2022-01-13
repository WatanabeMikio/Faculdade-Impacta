# Escreva um programa que receba como entrada dois números inteiros
#  quaisquer A e B e exiba todas 
# as tabuadas existentes no intervalo fechado crescente [ A..B ]

# Entrada
# Dois números inteiros, um em cada linha.
# 
# SAida
# As tabuadas de todos os valores inteiros no intervalo fechado crescente [ A..B ]. 
# Ao fim de cada tabuada, exibir uma linha com dez hifens ('-'). Caso A seja maior do que B,
#  o intervalo será vazio e, neste caso, deve ser exibida somente a frase 
# 'Nenhuma tabuada no intervalo!', sem apóstrofos. Obs.: Lembre-se de não exibir texto no input.

def tabuada(A,B):
    
    while A <= B:
        n = 1
        while n <= 10:
            tabuada = A * n
            print (f'{A} x {n} = {tabuada}')
            n += 1
        print ('-'*10)
        A += 1
    return


A = int(input('a = '))
B = int(input('b = '))
n = 1


if A > B:
   print ('Nenhuma tabuada no intervalo!')

tabuada (A,B) 
