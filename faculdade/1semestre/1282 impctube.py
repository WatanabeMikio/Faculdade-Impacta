def inserir(qtd_canais):
    tabela_de_canais = []
    for i in range(qtd_canais):
       nome, inscritos, monetizacao, premium = input().split(';')
       inscritos = int(inscritos)
       monetizacao = float(monetizacao)
       premium = premium == 'sim'
       tabela_de_canais.append([nome, inscritos, monetizacao, premium])
    return tabela_de_canais

def valor_bonus(tabela_de_canais, premium, nao_premium):
    bonus = []
    for linha in tabela_de_canais:
        valor = linha[2]
        if linha[3]:
            valor += linha[1] // 1000 * premium
        else:
            valor += linha[1] // 1000 * nao_premium
        bonus.append([linha[0], valor])
    return bonus

def exibir(calculo_bonus):
    print(5 * '-')
    print('BÔNUS')
    print(5 * '-')
    for linha in calculo_bonus:
        print(f'{linha[0]}: R$ {linha[1]:.2f}')


qtd_canais = int(input())
tabela_de_canais = inserir(qtd_canais)
premium = float(input())
nao_premium = float(input())
calculo_bonus = valor_bonus(tabela_de_canais, premium, nao_premium)
exibir (calculo_bonus)





   