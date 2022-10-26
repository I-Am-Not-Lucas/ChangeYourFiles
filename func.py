import os
import shutil 
import sys

def testa_escolha(escolha): 
    opcoes_funcionais =  ['1', '2', '3']

    if escolha in opcoes_funcionais:
        return True
    else:
        return False
    


def path_test(caminho):
    try:
        os.chdir(caminho)
        arquivo = open("test_application.txt", "a+")
        arquivo.writelines("Testando o caminho...\n")
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
  
    for root, dirs, files in os.walk(caminho):
        for file in files:
            try:
                name, ext = os.path.splitext(file)
                new_name = name.capitalize() + ext
                source = caminho + f'\\{file}'
                destiny = caminho + f'\\{new_name}'
                os.rename(source, destiny)
                count += 1

            except FileNotFoundError:
                pass
            
            except:
                print("Algo deu errado...")
    if count > 0:
        print(f'{count} arquivo(s) renomeado(s) com sucesso')
    else:
        print("Nenhum arquivo foi alterado")


def lower_case(caminho):
    count = -1 
    for root, dirs, files in os.walk(caminho):
        for file in files:
            try:
                name, ext = os.path.splitext(file)
                new_name = name.lower() + ext
                source = caminho + f'\\{file}'
                destiny = caminho + f'\\{new_name}'
                os.rename(source, destiny)
                count += 1

            except FileNotFoundError:
                pass
            
            except:
                print("Algo deu errado...")
    if count > 0:
        print(f'{count} arquivo(s) renomeado(s) com sucesso')
    else:
        print("Nenhum arquivo foi alterado")

def upper_case(caminho):
    count = -1 
  
    for root, dirs, files in os.walk(caminho):
        for file in files:
            try:
                name, ext = os.path.splitext(file)
                new_name = name.upper() + ext
                source = caminho + f'\\{file}'
                destiny = caminho + f'\\{new_name}'
                os.rename(source, destiny)
                count += 1

            except FileNotFoundError:
                pass
            
            except:
                print("Algo deu errado...")
    if count > 0:
        print(f'{count} arquivo(s) renomeado(s) com sucesso')
    else:
        print("Nenhum arquivo foi alterado")

