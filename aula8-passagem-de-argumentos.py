import sys
import arg

argumentos = sys.argv

#print(argumentos)

def soma(n1,n2):
    return float(n1) + float(n2)

try:
    if argumentos[1] == "soma":
        print(soma(argumentos[2],argumentos[3]))
except:
    print("Uso: "+argumentos[0]+" soma n1 n2")