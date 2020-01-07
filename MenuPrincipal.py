import re
import datetime
def gestaoFuncionario():
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
    while True:
        x = input('Escolha uma das opções: ')
        if x == '0':
            InserirFuncionario()
        elif x == '1':
            InserirFuncionario()
        elif x == '2':
            InserirFuncionario()
        elif x == '3':
            InserirFuncionario()
        elif x == '4':
            InserirFuncionario()
        elif x == '5':
            InserirFuncionario()
        elif x == '6':
            InserirFuncionario()
        elif x == '7':
            InserirFuncionario()
        elif x == '8':
            InserirFuncionario()
        elif x == '9':
            InserirFuncionario()
        elif x == '10':
            InserirFuncionario()
        else:
            print("Esta opção é inválida!")

def InserirFuncionario():
    nomeficheiro = "dados/funcionarios.txt"
    IDFuncionario = 2
    IDCategoria = 0  # input("ID Categoria? ")
    IDTitulo = 0  # input("ID Título? ")
    IDServico = 0  # input("ID Serviço? ")
    IDFuncionarioChefe = 0  # input("ID Funcionário Chefe? ")

    while True:
        CdFuncionario = input("Código do Funcionário? ")
        if re.search(
            "[A-Z]{1,10}", 
            CdFuncionario
            ) :
            break
        else:
            continue

    while True:
        NmFuncionario = input("Nome Funcionário? ")
        if re.search(
            "^[A-Z][a-zA-Z]{3,}(?: [A-Z][a-zA-Z]*){0,4}$", 
            NmFuncionario
            ) :
            break
        else:
            continue

    while True :
        Email = input("Email? ")
        if re.search(
            "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", 
            Email
            ) :
            break
        else:
            continue

    while True:
        Telemovel = input("Telemóvel? ")
        if re.search(
            "9[1236]\d{7}", 
            Telemovel
            ) :
            break
        else:
            continue

    while True:
        NIF = input("NIF? ")
        if idValidNIF(NIF):
            break
        else:
            continue

    while True:
        NCC = input("Número de Cartão de Cidadão? ")
        if isValidNCC(NCC) :
            break
        else:
            continue

    while True :
        DataAdmissao = input("Data de Admissão? ")
        if isDataAnterior(DataAdmissao) == '0' :
            break
        else:
            continue

    while True:
        Vencimento = input("Vencimento? ")
        if re.search(
            "[0-9]\d{8},[0-9]\d{2}", 
            Vencimento
            ) :
            break
        else:
            continue

    f = open(nomeficheiro, "at")
    print(
        IDFuncionario,
        CdFuncionario,
        NmFuncionario,
        IDCategoria,
        IDTitulo,
        IDServico,
        IDFuncionarioChefe,
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

def isValidNCC(str):
    return True

def idValidNIF(num):
    return True

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

gestaoFuncionario()