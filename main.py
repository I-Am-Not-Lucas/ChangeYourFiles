
from func import *


print("Choose a option")
print("[1] Captilize")

caminho = ("C:\Programacao\Python\PROJETOS\ChangeYourFiles\pasta_testes")
caminho = caminho.replace("\\", "\\\\")
path_test(caminho)

escolha = '1'


while True:
    if escolha == '1':
        capitalize()
        break
    else:
        print("opção inválida")
        break

