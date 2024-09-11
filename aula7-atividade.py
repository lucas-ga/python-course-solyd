# Escreva uma função que recebe um objeto de coleção
# e que retorne o valor do maior número dentro dessa coleção.
# Faça outra função que retorna o menor número dessa coleção.

def verifica_maior_valor(lista):
    maior = 0
    for item in lista:
        if item > maior:
            maior = item
        
    return maior

def verifica_menor_valor(lista):
    menor = 0
    contador = 0
    for item in lista:
        contador += 1
        if item < menor or contador == 1:
            menor = item
    
    return menor


lista = {4,23,2,45,88}

print('O maior valor é',verifica_maior_valor(lista))

print('O menor valor é',verifica_menor_valor(lista))