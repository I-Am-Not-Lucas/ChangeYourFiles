import os
import shutil 

def capitalize():
    pass

def path_test(caminho):
    try:
        os.mkdir(caminho)

    except Exception as e:
        print("Invalid path")
        print(e)

    else:
        print(f"caminho {caminho} é válido")


