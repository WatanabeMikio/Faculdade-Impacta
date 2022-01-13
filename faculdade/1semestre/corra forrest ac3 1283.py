lista_de_tempos = []
soma_dos_tempos = 0
tempo = 1
while tempo > 0:
    tempo = (int(input('tempo em segundos ')))
    lista_de_tempos.append(tempo)
    if tempo < 0:
        lista_de_tempos.pop()
        break

for tempo in lista_de_tempos:
    soma_dos_tempos +=  tempo

media = soma_dos_tempos / len(lista_de_tempos)

print(f'Media: {media:.2f}')

for tempo in lista_de_tempos:
    if tempo < media:
        print(f'{tempo}')