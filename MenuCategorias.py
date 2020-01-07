# -*- coding: utf-8 -*-
def Menu(Titulo, Opcoes, np):
    print(Titulo)
    print()
    for i in range(np):
        print(i + 1, "-", Opcoes[i])
    print("0 - Terminar")
    while True:
        print("Opção?")
        op = int(input())
        if (op >= 0 and op <= np):
            break
    return op


def LerNumeroInteiro0(msg, min, max):
    while True:
        n = int(input(msg))
        if n >= min and n <= max:
            break
        else:
            print ("O valor deve estar entre %d e %d" % (min, max))
    return n


def LerNumeroInteiro1(msg, min, max):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print ("Não digitou um número inteiro!")
            continue
        if n >= min and n <= max:
            break
        else:
            print ("O valor deve estar entre %d e %d" % (min, max))
    return n

# ns = LerNumeroInteiro1("Número sócio?", 0, 100)

def LerNumero(msg, min, max, tipo = "inteiro"):
    # tipo in ["inteiro", "real"]
    while True:
        try:
            if tipo=="inteiro":
                n = int(input(msg))
            else:
                n = float(input(msg))
        except ValueError:
            print ("Não digitou um número inteiro!")
            continue
        if n >= min and n <= max:
            break
        else:
            print ("O valor deve estar entre %d e %d" % (min, max))
    return n
# ni = LerNumero("Número sócio?", 0, 100)
# print(type(ni))
# ni = LerNumero("Número sócio?", 0, 100, "inteiro")
# print(type(ni))
# nr = LerNumero("Número sócio?", 0, 100, "real")
# print(type(nr))
# exit();


def LerData(msg, min=None, max=None):
    from datetime import datetime
    while True:
        data_texto = input(msg)
        try:
            data = datetime.strptime(data_texto, '%Y-%m-%d')
        except ValueError:
            print("Data inválida")
            continue
        if data >= min and data <= max:
            break;
        else:
            print("Data fora do intervalo %s e %s"
                  % (min.strftime ("%Y-%m-%d"),
                     max.strftime ("%Y-%m-%d")))

from datetime import datetime
data_nas = LerData("Data ns",
                   datetime.strptime("0001-01-01", '%Y-%m-%d'),
                   datetime.strptime("9999-12-12", '%Y-%m-%d'))

import re

def ValidaNome(nome):
    if re.search("^[A-Z][a-z]{1,10} [A-Z][a-z]{1,10}", nome):  # No match
        return True
    return False

def ValidaCodigo(codigo, tamanho_min, tamanho_max):
    if re.search("^[A-Z0-9]{2,10}", codigo):  # No match
    # if re.search("^[A-Z0-9]{%d,%d}" % (tamanho_min, tamanho_max), codigo):  # No match
        t = len(codigo)
        if t >= tamanho_min and t <= tamanho_max:
            return True
    return False

def ValidaEMail(email):
    if re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):  # No match
        return True
    return False

def LerNome(legenda):
    while True:
        nome = input(legenda)
        if ValidaNome(nome):
            return nome
        else:
            print("Nome inválido")

def LerCodigo(legenda):
    while True:
        codigo = input(legenda)
        if ValidaCodigo(codigo):
            return codigo
        else:
            print("Código inválido")

# Aula 30 out 2019
#  Python - importar módulos
#  Validação de dados Python expressões regulares
# https://moodle.ipg.pt/pluginfile.php/112547/mod_resource/content/1/re_match.py

#
# Aula 4 nov 2019
# Many Ways for a Nicer Output
#  main_OT3_2017.pdf: Entrada e validação de dados
#  Exemplo python validação dados: numero, data
    #  https://moodle.ipg.pt/mod/resource/view.php?id=28841
#  Notas com validação de nomes (regex), Nomes, silgas


def InserirCategoria():
    # 3 / 20 - sem valiadação
    print ("Inserir Categoria:")
    # IDCategoria = int(input("ID ?"))      # sem validação
    IDCategoria = LerNumero("ID?", 1, 99)   # com validação
    # CdCategoria = input("Código?")          #
    CdCategoria = Ler
    # NmCategoria = input("Nome?")
    NmCategoria = LerNome("Nome?")

    f = open("Categorias.csv")
    print(IDCategoria, CdCategoria,NmCategoria, file=f, sep=';')
    f.close()


n =  LerNumeroInteiro0("sdsd", 1, 99)
def MenuCategorias():
    while True:
        op = Menu("Menu categorias", ["Inserir","Listar todos",
             "Pesquisa por nome","Alterar","Eliminar"], 5)
        if op == 0:
            break
        elif op == 1:
            InserirCategoria()
        elif op == 2:
            ListarCategorias()
        elif op == 3:
            PesquisaCategoriaNome()
        elif op == 3:
            AlterarCategoria()
        elif op == 3:
            EliminarCategoria()

MenuCategorias()