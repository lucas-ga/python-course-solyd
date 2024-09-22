"""
Autor: Lucas Silva
Script criado com o intuito de auxiliar na instalação de programas onde possui somente os binários
"""
import argparse
import glob
import os
import shutil
import sys

from sympy.physics.units import action

APPLICATIONS_DIR = '/usr/share/applications/'

if os.getuid() != 0:
    print("This script needs to be run as root (use sudo).")
    sys.exit(1)

os.system('clear')

print("""
  _   _               _        ___     ___            
 | | | |   _ _       (_)      | _ \   |_ _|    _ _    
 | |_| |  | ' \      | |      |  _/    | |    | ' \   
  \___/   |_||_|    _|_|_    _|_|_    |___|   |_||_|  
_|\"\"\"\"\"| _|\"\"\"\"\"| _|\"\"\"\"\"| _| \"\"\" | _|\"\"\"\"\"| _|\"\"\"\"\"| 
"`-0-0-' "`-0-0-' "`-0-0-' "`-0-0-' "`-0-0-' "`-0-0-' 

[ Universal Program Installer ]
""")

parser = argparse.ArgumentParser(
    prog='Unipin',
    description='Script created to help with programs instalation',
    usage='unipin[.py] [options] [-d /path/to/file] filename',
    allow_abbrev=False
)

parser.add_argument('filename')
parser.add_argument('-b','--basic',default=False, help='Only add shortcut to menu', required=False, action='store_true')
parser.add_argument('-d','--directory', help='Directory with program files', required=False, default=os.getcwd())
parser.add_argument('--no-path',default=False, help='Don\'t add program to Path', required=False, action='store_true')
parser.add_argument('--no-icon',default=False, help='Don\'t add icon to program',required=False, action='store_true')
parser.add_argument('-v','--version',action='version',version='%(prog)s 1.0')
args = parser.parse_args()

dict_args = vars(args)

if dict_args.get('directory') and not os.path.isdir(dict_args.get('directory')):
    print(f"Erro: O diretório {dict_args.get('directory')} não existe.")
    sys.exit(1)

basic = dict_args.get('basic')

filename = dict_args.get('filename')
pgm_name = filename
pgm_desc = ''
icon_path = ''
categorias_str = ''
file_path = ''
if not basic:
    pgm_name = input('Qual será o nome do programa? ')
    pgm_desc = input('Informe a descrição do programa: ')
    if not dict_args.get('no_icon'):
        img_extensions = ['png', 'jpg', 'jpeg', 'bmp', 'gif']
        img_files = {}
        if dict_args.get('directory') != '':
            file_path = dict_args.get('directory')
        else:
            file_path = os.getcwd()
        i = 0
        for ext in img_extensions:
            i += 1
            img_files[i] = (glob.glob(os.path.join(file_path, f'{pgm_name}.{ext}')))
        print('[0] - Nenhum')
        i = 0
        for i, files in img_files.items():
            print(f'[{i}] - {files[0]}' if files else f'[{i}] - Nenhum arquivo encontrado')
        icon = input('Selecione o icone:')
        if icon != '0':
            icon_path = img_files[int(icon)][0]
        os.system('clear')
        categories = [
            "AudioVideo", "Development", "Education", "Game", "Graphics", "Network",
            "Office", "Science", "Settings", "System", "Utility", "Audio", "Video",
            "AudioVideoEditing", "TextEditor", "Email", "FileTools", "FileManager",
            "TerminalEmulator", "Calculator", "Viewer", "Accessibility", "Documentation"
        ]
        print('Selecione as categorias do programa')
        for i, categoria in enumerate(categories, 1):
            print(f'[{i}] - {categoria}')
        escolha = input("Digite o(s) número(s) das categorias separadas por vírgula (ex: 1, 3, 5): ")
        indices_escolhidos = [int(i.strip()) for i in escolha.split(',') if i.strip().isdigit()]
        categorias_selecionadas = [categories[i - 1] for i in indices_escolhidos if 1 <= i <= len(categories)]
        if categorias_selecionadas:
            categorias_str = ";".join(categorias_selecionadas) + ";"

config_file = APPLICATIONS_DIR + filename + '.desktop'

os.system('clear')

# copia os arquivos para o diretório novo
dest_dir = f'/usr/share/{pgm_name}'
source_dir = file_path
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

for item in os.listdir(source_dir):
    source_item = os.path.join(source_dir, item)
    dest_item = os.path.join(dest_dir, item)

    if os.path.isdir(source_item):
        shutil.copytree(source_item, dest_item)  # Copia diretório recursivamente
    else:
        shutil.copy2(source_item, dest_item)  # Copia arquivos
    print(f"{item} copiado para {dest_item}")

# verificar se o comando abaixo abre arquivo com caminho relativo
try:
    with open(config_file, 'w') as file:
        # Conteúdo do arquivo .desktop
        file.write('[Desktop Entry]')
        file.write(f'\nName={pgm_name}')
        file.write(f'\nComment={pgm_desc}')
        file.write(f'\nExec=/usr/share/{pgm_name}/{pgm_name}')
        if icon_path:
            file.write(f'\nIcon={icon_path}')
        file.write(f'\nType=Application')
        file.write(f'\nCategories={categorias_str}')
except IOError as e:
    print(f"Erro ao criar o arquivo {config_file}. Verifique as permissões. Detalhes: {e}")

# adiciona ao path
if not dict_args.get('no_path'):
    bashrc_path = os.path.expanduser("~/.bashrc")
    with open(bashrc_path, "r") as file:
        if f'/usr/share/{pgm_name}/' not in file.read():
            with open(bashrc_path, "a") as file:
                file.write(f'export PATH="$PATH:/usr/share/{pgm_name}/"\n')

print(f"Arquivo {config_file} criado com sucesso.")