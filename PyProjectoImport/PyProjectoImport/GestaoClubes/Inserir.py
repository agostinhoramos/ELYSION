# import ValidacaoDados.ValidacaoDados
from ValidacaoDados.ValidacaoDados import *

def Inserir():
    nome = input("Nome clube ?")

    while True:
        nome = input("Nome ?")
        # if ValidacaoDados.ValidacaoDados.ValidaNome(nome):
        if ValidaNome(nome):
            break
        print("Nome inválido")
