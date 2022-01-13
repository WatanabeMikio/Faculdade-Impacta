# Programação Orientada a Objetos
# AC01 ADS-EaD - Números especiais
#
# Email Impacta: tiago.watanabe@aluno.faculdadeimpacta.com.br


def eh_primo(n):

    qtd_divisores = 0
    candidato = 1
    while candidato <= n:
        if n % candidato == 0:
            qtd_divisores += 1
        candidato += 1

    if qtd_divisores == 2:
        return True
    else:
        return False

    pass


def lista_primos(n):

    numeros_primos = []
    for i in range(2, n):
        if eh_primo(i):
            numeros_primos.append(i)
    return numeros_primos

    pass


def conta_primos(s):
    dicionarios_primos = {}
    for numero in range(len(s)):
        if eh_primo(s[numero]):
            if s[numero] in dicionarios_primos:
                dicionarios_primos[s[numero]] += 1
            else:
                dicionarios_primos[s[numero]] = 1
    return dicionarios_primos
    pass


def eh_armstrong(n):

    n = str(n)
    lista_soma = []
    num_digitos = len((n))
    for numero in range(0, num_digitos):
        multi = int(n[numero]) ** num_digitos
        lista_soma.append(multi)
        soma = sum(lista_soma)
    if soma == int(n):
        return True
    else:
        return False
    pass


def eh_quase_armstrong(n):

    n = str(n)
    lista_soma = []
    num_digitos = len((n))
    for numero in range(0, num_digitos):
        multi = int(n[numero]) ** num_digitos
        lista_soma.append(multi)
        soma = sum(lista_soma)
    if soma == int(n) - 1:
        return True
    else:
        return False
    pass


def lista_armstrong(n):
    lista_armstrong_menor = []
    for armstrong in range(0, n):
        if eh_armstrong(armstrong):
            lista_armstrong_menor.append(armstrong)
    return lista_armstrong_menor
    pass


def eh_perfeito(n):
    lista_divisores = []
    for num in range(1, n):
        if n % num == 0:
            lista_divisores.append(num)
    soma_divisores = sum(lista_divisores)
    if soma_divisores == n:
        return True
    else:
        return False
    pass


def lista_perfeitos(n):
    lista_perfeitos_menor = []
    for num in range(2, n):
        if eh_perfeito(num):
            lista_perfeitos_menor.append(num)

    return lista_perfeitos_menor
    pass
