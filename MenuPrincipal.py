# -*- coding: utf-8 -*-

NomeFicheiroServicos = "servicos.csv"

def Menu(Titulo, Opcoes, np):
    print(Titulo)
    print()
    for i in range(np):
        print( i + 1 , " - ", Opcoes[i])
    print( "0 - Terminar")
    while True:
        print("Opção?")
        op = int(input())
        if (op >= 0 and op <= np):
            break
    return op

def InserirServico():
    # Ler dados
    # Abir ficheiro
    # Escrever dados no fim
    # fechar ficheiro
    print ("Inserir Serviço:")
    # Ler dados
    IDServico = int(input("ID?"))
    NmServico = input("Nome ?")
    NumeroFuncionarios = int(input("Número de funcionarios ?"))
    IDFuncionarioResponsavel = int(input("ID Responsavel?"))
    # Abir ficheiro
    f = open (NomeFicheiroServicos, "at")
    print(IDServico, NmServico, NumeroFuncionarios,
          IDFuncionarioResponsavel, file=f, sep=";")
    f.close()
def ListarServicosTodos ():
    f = open(NomeFicheiroServicos, "rt")
    servicos = f.readlines()
    f.close()
    print(servicos)
    for i in range(len(servicos)):
        ID, Servico, NF, IDResponsavel = servicos [i].split(";")
        IDResponsavel =  IDResponsavel.strip('\n')
        print(ID, Servico, NF, IDResponsavel)

def ExportarServicosTodosHTML ():
	import os
        f = open(NomeFicheiroServicos, "rt")
        servicos = f.readlines()
        f.close()
        f = open("ServicosTodos.html", "wt")
    print("<table>", file=f)
    for i in range(len(servicos)):
        ID, Servico, NF, IDResponsavel = servicos [i].split(";")
        IDResponsavel =  IDResponsavel.strip('\n')
        print("<tr>", file=f)
        print("<td>", ID, "</td>", file=f)
        print("<td>", Servico , "</td>", file=f)
        print("<td>", NF, "</td>", file=f)
        print("<td>", IDResponsavel , "</td>", file=f)
        print("</tr>", file=f)
	print("</table>", file=f)
	f.close()
	os.exec("ServicosTodos.html")


def PesquisaServicosNome ():
    f = open(NomeFicheiroServicos, "rt")
    servicos = f.readlines()
    f.close()
    nomeProcurar = input("Nome a procurar")
    for i in range(len(servicos)):
        ID, Servico, NF, IDResponsavel = servicos [i].split(";")
        Servico = str(Servico)
        IDResponsavel =  IDResponsavel.strip('\n')
        #if nomeProcurar == Servico:   #pesquisa exata
			#print(ID, Servico, NF, IDResponsavel)
			#break
        if Servico.find(nomeProcurar) >= 0:     # serviço contem texto nomeProcurar
            print("%4d %-30s %2d %4d" % (ID, Servico, NF, IDResponsavel))

def LerServicosVetor():
  f = open(NomeFicheiroServicos, "rt")
  servicos = f.readlines()
  f.close()
  return servicos

def PesquisaServicosNF ():
	# lista serviços com NP entre dois valores min, max
	servicos = LerServicosVetor()
    minNF = int (input("Mínimo de funcionários?"))
	maxNF = int (input("Máximo de funcionários?"))
    for i in range(len(servicos)):
        ID, Servico, NF, IDResponsavel = servicos [i].split(";")
        Servico = str(Servico)
		NF = int(NF)
        IDResponsavel =  IDResponsavel.strip('\n')
        if NF >= minNF and NF <= maxNF: 
            print("%4d %-30s %2d %4d" % (ID, Servico, NF, IDResponsavel))

def MenuGestaoServicos():
    Titulo = "Gestão de Servicos"
    Opcoes = ["Inserir", "Alterar", "Eliminar", "Listar todos", "Pesquisa por nome",
              "Pesquisar por número de funcionários"]
    np  = 6
    while True:
        op = Menu(Titulo, Opcoes, np)
        if op == 1:
            InserirServico()
        elif op == 2:
            print(op)
            #PesquisarServicoPorNome()
        if op == 4:
            ListarServicosTodos()
        if op == 5:
            PesquisaServicosNome()
        elif op == 0:
            break;

def MenuPrincipal():
    Titulo = "Menu principal"
    Opcoes = ["Gestão de Serviços", "Gestão de  Categorias",
              "Gestão de Títulos", "Gestão dos Funcionários", "..."]
    np  = 5
    while True:
        op = Menu(Titulo, Opcoes, np)
        if op == 1:
            MenuGestaoServicos()
        elif op == 2:
            print (op)
            # GestaoPaises()
        elif op == 0:
            break
MenuPrincipal()