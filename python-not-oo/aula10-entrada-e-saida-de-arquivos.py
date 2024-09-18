from os import close

arquivo = open('/home/lucasgs/arquivo.txt','w')

for i in range(0, 100):
    arquivo.write(str(i))

arquivo = open('/home/lucasgs/arquivo.txt')

print(arquivo.read())