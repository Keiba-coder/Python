Salas = [[28, 31, 34, 33], [25, 27, 29, 28],  [32, 35, 36, 34],[24, 26, 25, 27]]

sala_com_mais_criticos = 0
max_criticos = -1

for num in range(len(Salas)):
    sala_atual = Salas[num]
    numero_sala = num + 1

    media = sum(sala_atual) / len(sala_atual)

    criticos = 0
    for temp in sala_atual:
        if temp >= 33:
            criticos += 1

    print(f"\nSala {numero_sala}: Média = {media:.1f}°C - Registros Críticos: {criticos}")

    if criticos > max_criticos:
        max_criticos = criticos
        sala_com_mais_criticos = numero_sala

print(f"\nA sala com a maior quantidade de registros críticos foi a Sala {sala_com_mais_criticos}.")