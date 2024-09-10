nome = input('Escreva seu nome')
idade = 25
altura = 1.74
tipo = type(nome)
tipo2 = type(idade)
tipo3 = type(altura)

print('Hello World!\nSegundo print')
print('\n'+str(tipo))
print('\n'+str(tipo2))
print('\n'+str(tipo3))

print('\n',tipo,tipo2,tipo3,type(tipo))

try:
    print('\n'+tipo3)
except:
    print('erro')