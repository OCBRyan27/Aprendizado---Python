jogos = ["Undertale", "Deltarune", "Zenless Zone Zero"]
jogos.append("My Dystopian Robot Girlfriend")

print(jogos[0])
posicao = len(jogos)
print("O tamanho da lista é:", posicao)

#O Índice Negativo (-1)
#Em vez de contar os itens para saber qual é o último índice (0, 1, 2, 3...), no Python você pode 
# usar o -1. Ele faz o caminho inverso e pega o último elemento da lista, não importa o tamanho dela!
#print(jogos[-1])  #ÚLTIMO item: My Dystopian Robot Girlfriend
#Se você quiser o penúltimo, basta usar -2, e assim por diante.