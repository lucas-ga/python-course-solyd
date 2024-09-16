import time


try:
    a = 1200 / 0
except Exception as erro:
    print('erro divisao por zero -',erro)

def abre_arquivo(arquivo):
    try:
        open(arquivo)
        return True
    except:
        print('erro ao abrir arquivo, tentando novamente em 5 segundos')
        time.sleep(5)
        return False
    
while not abre_arquivo():
    print('Tentando abir arquivo')

print('abriu arquivo')