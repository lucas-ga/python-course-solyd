# Formulario que pergunta nome, cpf, endereco, idade, altura e telefone e imprima em uma relatorio organizado

import os

from progress.bar import Bar
from time import sleep

print('Bem vindo ao Cadastro Cidadão!\n')

nome = input('Informe seu nome:')
cpf = input('Informe seu cpf:')
endereco = input('Informe seu endereço:')
altura = input('Informe sua altura:')
telefone = input('Informe seu telefone:')

os.system('cls' if os.name == 'nt' else 'clear')

print('Obrigado pelas informações, estamos processando seu cadastro no banco de dados.\n')

with Bar('Processando...') as bar:
    for i in range(100):
        sleep(0.02)
        bar.next()

os.system('cls' if os.name == 'nt' else 'clear')

print('Cadastro finalizado, confira os dados abaixo e pressione ENTER\n')

formulario = 'Nome: '+nome+'\nCPF: '+cpf+'\nEndereço: '+endereco+'\nAltura: '+altura+'\nTelefone: '+telefone

print(formulario)

input()

os.system('cls' if os.name == 'nt' else 'clear')