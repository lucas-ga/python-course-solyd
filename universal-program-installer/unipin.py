"""
Autor: Lucas Silva
Script criado com o intuito de auxiliar na instalação de programas onde possui somente os binários

Argumentos aceitos:
-h help
-b --basic: Configuração básica, somente incluindo o item no menu
--nopath: Não adiciona o programa ao Path
--noicon: Não adiciona o icone do programa
"""
import argparse
import re

parser = argparse.ArgumentParser(
    prog='unipin[.py]',
    description='Script created to help with programs instalation',
    epilog='O menu de ajuda é exibido automaticamente no caso de erro na leitura dos parâmetros',
    usage='%(prog)s [options] [-d /path/to/files] filename'
)

parser.add_argument('filename')
parser.add_argument('-b','--basic',help='Only adds to menu')
parser.add_argument('-d','--directory',help='directory')
parser.add_argument('--nopath',default='false')
parser.add_argument('--noicon',default='false')
parser.print_help()


nome_programa = ''
arquivo_imagem = ''
arquivo_binario = ''
tags = []
basic = False
path = True
icon = True
help_menu = False

file_name = args[0]

# valida o parâmetro -b
contador = 0
if len(args) > 1:
    for item in args:
        contador += 1
        if len(args) > 2:
            if re.match("^-h$", item) or re.match("^--help$", item):
                help_menu = True
                break
            if re.match("^-*b*$", item) or re.match("^--basic$", item):
                basic = True
            if re.match("^--nopath$", item):
                path = False
            if re.match("^--noicon$", item):
                icon = False
        if contador == len(args):
            arquivo_binario = item
            try:
                open('b',arquivo_binario)
            except:
                help_menu = True
else:
    help_menu = True

if help_menu:
    print("""
Uso: """+file_name+""" [Argumentos] [-h --help | -b --basic] ... [arquivo_binario]

Argumentos aceitos:
-h --help  : Abre o menu de ajuda
-b --basic : Configuração básica, somente incluindo o item no menu
--nopath   : Não adiciona o programa ao Path
--noicon   : Não adiciona o icone do programa
    """)
else:
    nome_programa = input('Qual será o nome do programa?')
    if re.match('^[^0-9a-zA-Z]+$',nome_programa):
        nome_programa = arquivo_binario
    if icon and not basic:
        arquivo_imagem = input("Informe o caminho para o arquivo de imagem:")
    for i in range(10):
        i += 1
        tag = (input(f"Informe a tag {i}:"))
        if re.match('[0-9a-zA-Z]',tag):
            tags.append(tag)
        else:
            break
    print("tags:")
    for item in tags:
        print(item)

    print("arquivo binário:", arquivo_binario)
    print("nome programa:", nome_programa)
    print("imagem:", arquivo_imagem)