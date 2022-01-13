# Sua tarefa é construir um programa que receba como entrada um número natural N (0 <= N <= 10) e exibir a tabuada de N de 1 até 10.

# Entrada

# Um número natural N (0 <= N <= 10).

# Saída

# Exibir a tabuada do valor dado na entrada, conforme o modelo de saída dos exemplos.

i = 1
n = int(input('multi:'))
if 0 <= n <= 10:
    while 0 <= i <= 10:
        q = n * i
        print(f'{n} x {i} = {q}')
        i = i + 1