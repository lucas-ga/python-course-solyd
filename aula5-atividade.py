# Programa que leia a quantidade de pessoas que serão convidadas para uma festa.
# Após isso o programa irá perguntar o nome de todas as pessoas e colocar numa lista de convidadoss
# Após isso irá imprimir todos os convidados

import os

print('Bem vindo ao convidador de pessoas\n')

qtd_convidados = input('Quantas pessoas pretende convidar? (Anões e crianças contam como uma pessoa inteira)\nTotal: ')

lista_convidados = []
contador = 0

for i in range(int(qtd_convidados)):
    contador += 1
    nome = input('Nome convidado '+str(contador)+': ')
    lista_convidados.append(nome)

os.system('cls' if os.name == 'nt' else 'clear')

print('\nConfirme abaixo se todos os convidados estão na lista e pressione ENTER para confirmar\n')

contador = 0
for nome in lista_convidados:
    contador += 1
    print('Convidado '+str(contador)+': '+nome)

input()