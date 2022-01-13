def troca_inteiro(lista):
    for i in range(len(lista)):
        lista[i] = int(lista[i])

def exibir (produto):
    for i in range (len(produto)):
        if i < len(produto) - 1:
            print(produto[i], end= ' ')
        else:
            print(produto[i])

produto = input().split()
if produto != []:
    troca_inteiro(produto)

acao = input().split()

while acao[0] != 'encerrar':
    if acao[0] == 'adicionar':
        produto.append(int(acao[1]))
    elif acao[0] == 'remover':
        acao[1] = int(acao[1])
        if acao[1] in produto:
            produto.remove(acao[1])
        else:
            print(f'código {acao[1]} não encontrado')
    else:
        produto.sort()
        exibir(produto)
    acao = input().split()

produto.sort()
exibir(produto)

