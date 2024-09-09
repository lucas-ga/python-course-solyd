frase = 'oiiii, como vai'
lista_nomes = ['Joao','Maria','Guilherme','Lucas','Diego']
pais = 'Cuba'
frase2 = 'Ate cubanos'

#print(type(lista_nomes)) #retorna class 'list'

print(lista_nomes[0]) # retorna o conteudo do indice 0

print(pais[0:2]) # seleciona um range na lista

print(frase2[::-1]) # inverte a lista

lista_nomes.append('Valkiria') # adiciona item ao final da lista

print(lista_nomes)

lista_nomes.remove('Guilherme') # remove item, buscando por conteudo

print(lista_nomes)

lista_nomes.insert(0, 'Primeirilson') # adiciona item na posição indicada

print(lista_nomes)

lista_nomes.append('Valkiria') # adiciona item ao final da lista

print(lista_nomes.count('Valkiria'),'Valkirias') # conta a quantidade, buscando por conteudo

print(lista_nomes)

print(lista_nomes.pop()) # retorna o ultimo da lista e remove

print(lista_nomes)