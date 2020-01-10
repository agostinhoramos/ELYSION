# REGX: https://regex101.com/
import re
import datetime
import string

from Fn import isValid
from Fn import inFile

def menu():
    print("1 - Inserir")
    print("2 - Pesquisar")
    print("3 - Alterar")
    print("4 - Eliminar")
    print("5 - Pesqusar e Ordenar")
    print("6 - Contar")
    print("7 - Agrupar")
    print("8 - Agrupar e Contar")
    print("9 - Exportar")
    print("10 - Gerar Organogramas")
    print("0 - Sair")

    opc = '0'
    while opc == '0' :
        x = input('Escolha uma das opções: ')
        if x == '1':
            Inserir()
        elif x == '2':
            Pesquisar()
        elif x == '3':
            Alterar()
        elif x == '4':
            Eliminar()
        elif x == '5':
            PesquisarOrdenar()
        elif x == '6':
            Contar()
        elif x == '7':
            Agrupar()
        elif x == '8':
            AgruparContar()
        elif x == '9':
            Exportar()
        elif x == '10':
            GerarOrganograma()
        elif x == '0':
            opc = '1'
        else:
            print("Esta opção é inválida!")
        
        if opc == '0':
            opc = input("Deseja sair (Sim-1 ou Não-0)? ")
        else:
            print("\n")



def Inserir():
    FileName = "Dados/Funcionarios.txt"
    ID = inFile.NextLine(FileName)
    IDCategoria = 0  # input("ID Categoria? ")
    IDTitulo = 0  # input("ID Título? ")
    IDServico = 0  # input("ID Serviço? ")
    IDChefe = 0  # input("ID Funcionário Chefe? ")

    while True:
        Cd = "ASDERFDSDE"#input("Código do Funcionário? ")
        if re.search(
            "[A-Z]{1,10}", 
            Cd
            ) :
            break
        else:
            continue

    while True:
        Nm = "Agostinho Ramos"#input("Nome Funcionário? ")
        if re.search(
            "^[A-Z][a-zA-Z]{3,}(?: [A-Z][a-zA-Z]*){0,4}$", 
            Nm
            ) :
            break
        else:
            continue

    while True :
        Email = "agostinhopina95@gmail.com"#input("Email? ")
        if re.search(
            "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", 
            Email
            ) :
            break
        else:
            continue

    while True:
        Telemovel = "934927329"#input("Telemóvel? ")
        if re.search(
            "9[1236]\d{7}", 
            Telemovel
            ) :
            break
        else:
            continue

    while True:
        NIF = "287273962"#input("NIF? ")
        if isValid.NIF(NIF):
            break
        else:
            continue
        
    while True:
        NCC = "15547701 3 ZV1"#input("Número de Cartão de Cidadão? ")
        if isValid.NCC(NCC):
            break
        else:
            continue

    while True :
        DataAdmissao = input("Data de Admissão %Y-%m-%d %h %m %s? ")
        if isValid.DATE :
            break
        else:
            continue

    while True:
        Vencimento = "12.5"#input("Vencimento? ")
        if re.search(
            "([0-9])\d{,7}\.([0-9])\d{,1}", 
            Vencimento
            ) :
            break
        else:
            continue

    f = open(FileName, "at")
    print(
        ID,
        Cd,
        Nm,
        IDCategoria,
        IDTitulo,
        IDServico,
        IDChefe,
        Email,
        Telemovel,
        NIF,
        NCC,
        DataAdmissao,
        Vencimento,
        sep=";",
        file=f
    )
    f.close()
    print("Funcionário foi inserido com sucesso!")


def isDataAnterior(data_texto):
    dataAtual = datetime.date.today()
    formato = '%Y-%m-%d %h %m %s';

    try:
       data = datetime.strptime(data_texto, formato)
    except ValueError:
        print("Data inválida")

    if data <= dataAtual.strftime(formato):
        #if re.search("[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]", data_texto):
        #    print(1)
        #else :
        #    print(0)
        print('1')
    else:
        print('0')


# Others Importants Functions
def Pesquisar():
    return True

def Alterar():
    return True

def Eliminar():
    return True

def PesquisarOrdenar():
    return True

def Contar():
    return True

def Agrupar():
    return True

def AgruparContar():
    return True

def Exportar():
    return True

def GerarOrganograma():
    return True

#Be the last one!
menu()