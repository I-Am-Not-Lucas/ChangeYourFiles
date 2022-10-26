import os
import shutil 

def path_test(caminho):
    try:
        directory = "teste"
        parent_dir = caminho
        path = os.path.join( parent_dir, directory)
        os.mkdir(path)

    except FileExistsError:
        print("Caminho validado, teste já existente")

    except PermissionError:
        print("Sem permissão :(")

    except:
        print("Caminho inválido ou inexistente")
       

    else:
        print(f"caminho {caminho} é válido")


def trata_caminho(raw_path):
    caminho_tratado = raw_path.replace("\\", "\\\\")

    return caminho_tratado


def capitalize(caminho):
    count = 0 
    try:
        for root, dirs, files in os.walk(caminho):
            for file in files:
                name, ext = os.path.splitext(file)
                new_name = name.capitalize() + ext
                source = caminho + f'\\{file}'
                destiny = caminho + f'\\{new_name}'
                os.rename(source, destiny)
                count += 1
        print(f'{count} arquivo(s) renomeados com sucesso')
    except FileNotFoundError:
        print("Arquivos não encontrados")
                




