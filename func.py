import os
import shutil 
import sys

def testa_escolha(escolha): 
    opcoes_funcionais =  ['1']

    if escolha in opcoes_funcionais:
        return True
    else:
        return False
    


def path_test(caminho):
    try:
        os.chdir(caminho)
        arquivo = open("test_application.txt", "a+")
        arquivo.writelines("Testando o caminho...")
        arquivo.close()


    except FileExistsError:
        print("Caminho validado, teste já existente")


    except PermissionError:
        print("Sem permissão ")

    except Exception:
        print("Caminho inválido ou inexistente")


    else:
        print(f"caminho {caminho} é válido")


def trata_caminho(raw_path):
    caminho_tratado = raw_path.replace("\\", "\\\\")

    return caminho_tratado


def capitalize(caminho):
    count = -1 
    try:
        for root, dirs, files in os.walk(caminho):
            for file in files:
                name, ext = os.path.splitext(file)
                new_name = name.capitalize() + ext
                source = caminho + f'\\{file}'
                destiny = caminho + f'\\{new_name}'
                os.rename(source, destiny)
                count += 1

    except FileNotFoundError:
        print("Arquivos não encontrados")
    
    except:
        print("Algo deu errado...")

    else:
        print(f'{count} arquivo(s) renomeados com sucesso')




