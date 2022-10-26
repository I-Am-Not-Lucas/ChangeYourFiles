from func import *


print("Choose a option")
print('-' * 20)
print("[1] Captilize files")
print("[2] Lowercase - not working")
print("[3] Uppercase - not working")
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

else:
    print("Opção inválida ou fora do ar")

