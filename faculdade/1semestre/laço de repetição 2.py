# dados diversos numeros inteiros, exibir a media dos numeros lidos.
#  A entrada termina com a leitura do numero -1 que não deve ser contabilizado


soma = 0 
qtd = 0
n = int(input('Numero: '))

while n!= -1:
    soma += n
    qtd +=1
    n = int(input("numero: "))
    
print(f' Media {soma/qtd}')