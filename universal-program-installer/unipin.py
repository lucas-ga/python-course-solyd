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

parser = argparse.ArgumentParser(
    prog='Unipin',
    description='Script created to help with programs instalation',
    epilog='O menu de ajuda é exibido automaticamente no caso de erro na leitura dos parâmetros',
    usage='unipin[.py] [options] [-d /path/to/file] filename',
    allow_abbrev=False
)

parser.add_argument('filename')
parser.add_argument('-b','--basic',default=False, help='Only add shortcut to menu', required=False, action='store_true')
parser.add_argument('-d','--directory',help='directory with program files', required=False, action='store')
parser.add_argument('--no-path',default=False, help='Don\'t add program to Path', required=False, action='store_true')
parser.add_argument('--no-icon',default=False, help='Don\'t add icon to program',required=False, action='store_true')
parser.add_argument('-v','--version',action='version',version='%(prog)s 1.0')
args = parser.parse_args()

print(args)