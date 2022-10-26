from func import *


print("Choose a option")
print('-' * 20)
print("[1] Captilize files")
print("[2] Lowercase")
print("[3] Uppercase")
print('-' * 20)

escolha = input(">>> Opção: ")
situacao = testa_escolha(escolha)

if situacao:

    variavel_caminho = input((">>> Path: "))
    print('-' * 20)

    caminho = trata_caminho(variavel_caminho)
    path_test(caminho)


    if escolha == '1':
        capitalize(caminho)

    elif escolha == '2':
        lower_case(caminho)

    elif escolha == "3":
        upper_case(caminho)

else:
    print("Opção inválida ou fora do ar")

