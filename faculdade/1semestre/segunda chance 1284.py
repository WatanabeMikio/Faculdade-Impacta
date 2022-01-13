notas_originais = []
nota_alteradas = []

numeros_de_alunos = int(input('digite o numero de alunos:'))

if 0 <= numeros_de_alunos <= 999:
   
    for nota in range(0, numeros_de_alunos):
        primeira_nota = float(input('digita a primeira nota'))
        
        if primeira_nota >= 0 and primeira_nota <= 10:
            notas_originais.append(primeira_nota)
        else:
            notas_originais.append(0)

        if nota > numeros_de_alunos:
            break
    
    for nota in range(0, numeros_de_alunos):
        segunda_nota = float(input('digita a segunda nota'))
        
        if segunda_nota >= 0 and segunda_nota <= 10:
            nota_alteradas.append(segunda_nota)
        else:
            nota_alteradas.append(0)
        
        if nota > numeros_de_alunos:
            break

total_nota_alterada = 0
nota = 0
for nota in range(0, numeros_de_alunos):
    if nota_alteradas[nota] > notas_originais[nota] and nota_alteradas[nota] == 10:
        total_nota_alterada +=1
print (f'NOTAS ALTERADAS: {total_nota_alterada}')


for i in range(len(notas_originais)):
    nota_bonus = 0
    if notas_originais[i] < 9 and nota_alteradas[i] == 10:
        nota_bonus = notas_originais[i] + 2
        notas_originais[i] = '{0:.2f}'.format(notas_originais[i])
        nota_bonus = '{0:.2f}'.format(nota_bonus)
        print(f'*({i+1:03}) original: '+ str(notas_originais[i]).zfill(5) + ' | final: ' + str(nota_bonus).zfill(5))
      
    elif notas_originais[i] == 9 and nota_alteradas[i] == 10:
        nota_bonus = notas_originais[i] + 1
        notas_originais[i] = '{0:.2f}'.format(notas_originais[i])
        nota_bonus = '{0:.2f}'.format(nota_bonus)
        print(f'*({i+1:03}) original: '+ str(notas_originais[i]).zfill(5) + ' | final: ' + str(nota_bonus).zfill(5))
    else:
        notas_originais[i] = '{0:.2f}'.format(notas_originais[i])
        print(f'-({i+1:03}) original: '+ str(notas_originais[i]).zfill(5) + ' | final: ' + str(notas_originais[i]).zfill(5))

    
   


