# !/usr/bin/python3
# Programador: Nailalok_V4
# Data: 20/11/2024........
# Ferramenta: ZipLok......

import os
import zipfile
import time
import sys

def crack_zip_password(zip_path, wordlist_path):
    try:
        c = 0
        # Abre o arquivo zip
        with zipfile.ZipFile(zip_path, 'r') as zf:
            # Abre o arquivo wordlist
            with open(wordlist_path, 'r') as wordlist:
                # Lê cada senha da wordlist
                for line in wordlist:
                    c += 1
                    password = line.strip()
                    print(f'{c}-Testando senha: \033[33m{password}\033[m')  # Exibe a senha atual
                    try:
                        # Tenta extrair o arquivo com a senha atual
                        zf.extractall(pwd=password.encode())
                        print(f'\n\033[32;1mSenha encontrada:\033[m\033[36m {password}\033[m\n')
                        return
                    except RuntimeError:
                        # Se a senha estiver incorreta, continua com a próxima
                        continue
                    except RuntimeError as e:
                        print(f'\033[31mErro ao tentar a senha {password}: {e}\033[m')
                print('\033[31mSenha não encontrada na wordlist\033[m')
    except FileNotFoundError:
        print(f'\033[33mO arquivo zip: {zip_path}, não foi encontrado!\033[m')
    except Exception as e:
        print(f'\033[31mOcorreu um erro: {e}\033[m')

os.system("clear")
if len(sys.argv) < 2:
	print("python3 + crack_zip.py + nome_do_arquivo.zip")
	sys.exit()
# Caminhos para o arquivo zip e a wordlist
zip_path = sys.argv[1]
time.sleep(0.3)
print("Aguarde...\033[m")
time.sleep(0.8)

wordlist_path = 'wordlist.txt'    # Atualize com o caminho correto

# Chama a função de quebra de senha
crack_zip_password(zip_path, wordlist_path)
