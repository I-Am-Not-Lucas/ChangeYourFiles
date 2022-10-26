from func import *


# print("Choose a option")
# print()
# print("[1] Captilize")

variavel_caminho = input(("path >>>"))
caminho = trata_caminho(variavel_caminho)
# path_test(caminho)

escolha = '1'


while True:
    if escolha == '1':
        capitalize(caminho)
        break

    else:
        print("opção inválida")
        break

