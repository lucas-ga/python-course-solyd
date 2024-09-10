#Programa que pergunta o nome, idade, peso e altura e decide se está apta a entrar no exército
#Idade maior que 18, peso maior que 60kg e altura maior que 1,70m

print('Bem vindo ao cadastro de cortadores de grama\n\nPreencha as informações abaixo para ingressar no exército:\n')

nome = input('Nome: ')
idade = int(input('Idade: '))
peso = float(input('Peso: '))
altura = float(input('Altura: '))

if idade < 18:
    motivo = 'Idade'
elif peso < 60:
    motivo = 'Peso'
elif altura < 1.70:
    motivo = 'Altura'
else:
    motivo = ''

if motivo == '':
    print('\nBem vindo combatente')
else:
    print('Infelizmente você não cumpre os requisitos mínimos\n'+motivo+' inferior ao mínimo solicitado.')